# batch_bibtex.ps1 - 批量从 DBLP / arXiv 获取 BibTeX
# 优先 DBLP（直接出 .bib），arXiv 兜底（解析 Atom XML 构造 BibTeX）
# 用法: .\pyscripts\batch_bibtex.ps1

$InputFile = ".\preResearching\2.md"
$OutputFile = ".\batch_bibtex_output.bib"

# 解析论文标题
$titles = @()
Get-Content $InputFile -Encoding UTF8 | ForEach-Object {
    if ($_ -match '^\d+\.\s+(.+?)\s*\(.*?\)\s*(done)?$') {
        $titles += $Matches[1].Trim()
    }
}

Write-Host "Parsed $($titles.Count) papers`n" -ForegroundColor Cyan

function Search-DBLP {
    param([string]$Title)
    try {
        $encoded = [System.Uri]::EscapeDataString($Title)
        $url = "https://dblp.org/search/publ/api?q=$encoded&format=json&h=3"
        $resp = Invoke-RestMethod -Uri $url -Method Get -TimeoutSec 15 -ErrorAction Stop
        $hits = $resp.result.hits.hit
        if ($hits -and $hits.Count -gt 0) {
            $info = $hits[0].info
            $bibUrl = $info.url.TrimEnd('/') + ".bib"
            $bibResp = Invoke-WebRequest -Uri $bibUrl -TimeoutSec 15 -ErrorAction Stop -UseBasicParsing
            # .Content may return byte[], decode to string
            if ($bibResp.Content -is [byte[]]) {
                $bib = [System.Text.Encoding]::UTF8.GetString($bibResp.Content).Trim()
            } else {
                $bib = $bibResp.Content.Trim()
            }
            if ($bib.Length -gt 20) {
                return @{ Bib = $bib; Source = "DBLP"; Match = $info.title }
            }
        }
    } catch {}
    return $null
}

function Search-ArXiv {
    param([string]$Title)
    try {
        # 取标题关键词（去掉特殊字符），用 ti: 字段精确搜标题
        $clean = $Title -replace '[^a-zA-Z0-9\s]', ' '
        $clean = ($clean -split '\s+' | Where-Object { $_.Length -gt 2 }) -join '+AND+'
        $url = "http://export.arxiv.org/api/query?search_query=ti:$clean&max_results=3"
        $resp = Invoke-WebRequest -Uri $url -TimeoutSec 15 -ErrorAction Stop -UseBasicParsing
        if ($resp.Content -is [byte[]]) {
            $xmlText = [System.Text.Encoding]::UTF8.GetString($resp.Content)
        } else {
            $xmlText = $resp.Content
        }
        [xml]$xml = $xmlText

        $ns = @{ atom = "http://www.w3.org/2005/Atom" }
        $entries = $xml | Select-Xml -XPath "//atom:entry" -Namespace $ns

        if ($entries -and $entries.Count -gt 0) {
            $entry = $entries[0].Node
            $eTitle = ($entry.title -replace '\s+', ' ').Trim()
            $arxivId = ($entry.id -split 'abs/')[-1]
            $year = $entry.published.Substring(0, 4)
            
            # 提取作者
            $authors = @()
            foreach ($a in $entry.author) {
                $name = $a.name
                if ($name) { $authors += $name }
            }
            $firstAuthor = if ($authors.Count -gt 0) { $authors[0] } else { "Unknown" }
            $lastName = ($firstAuthor -split ' ')[-1].ToLower()

            # 构造 cite key
            $keyWord = ($eTitle -split '\s+')[0] -replace '[^a-zA-Z]', ''
            $citeKey = "${lastName}${year}${keyWord}".ToLower()

            # 构造 BibTeX
            $authorStr = $authors -join ' and '
            $bib = @"
@article{$citeKey,
  title     = {$eTitle},
  author    = {$authorStr},
  journal   = {arXiv preprint arXiv:$arxivId},
  year      = {$year},
  url       = {https://arxiv.org/abs/$arxivId}
}
"@
            return @{ Bib = $bib; Source = "arXiv"; Match = $eTitle }
        }
    } catch {}
    return $null
}

$results = @()
$failed = @()

for ($i = 0; $i -lt $titles.Count; $i++) {
    $title = $titles[$i]
    $num = $i + 1
    $shortTitle = if ($title.Length -gt 70) { $title.Substring(0, 70) + "..." } else { $title }
    Write-Host "[$num/$($titles.Count)] $shortTitle" -ForegroundColor White -NoNewline

    # --- 方法1: DBLP ---
    $result = Search-DBLP -Title $title

    # --- 方法2: arXiv (fallback) ---
    if (-not $result) {
        Start-Sleep -Seconds 1
        $result = Search-ArXiv -Title $title
    }

    if ($result) {
        $src = $result.Source
        $matchShort = if ($result.Match.Length -gt 50) { $result.Match.Substring(0, 50) + "..." } else { $result.Match }
        $results += "% Paper $num`: $title`n$($result.Bib)"
        Write-Host "  [$src] $matchShort" -ForegroundColor Green
    } else {
        $failed += [PSCustomObject]@{ Num = $num; Title = $title }
        Write-Host "  FAILED" -ForegroundColor Red
    }

    # Rate limiting: DBLP is generous, arXiv asks 3s between requests
    Start-Sleep -Seconds 3
}

# 写入输出
$header = "% Auto-generated BibTeX - $($results.Count) entries`n% Failed: $($failed.Count) entries`n"
$content = $header + "`n" + ($results -join "`n`n")
$outPath = Join-Path (Get-Location) $OutputFile
[System.IO.File]::WriteAllText($outPath, $content, [System.Text.Encoding]::UTF8)

Write-Host "`n$('=' * 60)" -ForegroundColor Cyan
Write-Host "OK: $($results.Count)/$($titles.Count)" -ForegroundColor Green
Write-Host "FAIL: $($failed.Count)/$($titles.Count)" -ForegroundColor Red
Write-Host "Output: $OutputFile" -ForegroundColor Cyan

if ($failed.Count -gt 0) {
    Write-Host "`nFailed:" -ForegroundColor Red
    foreach ($f in $failed) {
        Write-Host "  $($f.Num). $($f.Title)" -ForegroundColor Red
    }
}
