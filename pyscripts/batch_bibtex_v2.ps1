# batch_bibtex_v2.ps1 - 批量从 DBLP / arXiv 获取 BibTeX
# DBLP 优先（直接出 .bib），arXiv 兜底（构造 BibTeX）
# 用法: powershell -ExecutionPolicy Bypass -File .\pyscripts\batch_bibtex_v2.ps1

$ErrorActionPreference = "Continue"
$InputFile = ".\preResearching\2.md"
$OutputFile = ".\batch_bibtex_output.bib"
$LogFile = ".\batch_bibtex_log.txt"

# Log function: writes to both console and log file
function Log {
    param([string]$Msg, [string]$Color = "White")
    Write-Host $Msg -ForegroundColor $Color
    Add-Content -Path $LogFile -Value $Msg -Encoding UTF8
}

# Clear old log
if (Test-Path $LogFile) { Remove-Item $LogFile }

# 解析论文标题
$titles = @()
Get-Content $InputFile -Encoding UTF8 | ForEach-Object {
    $line = $_.Trim()
    if ($line -match '^\d+\.\s+(.+?)\s*\(.*?\)\s*(done)?$') {
        $titles += $Matches[1].Trim()
    }
}

Log "Parsed $($titles.Count) papers" Cyan

$results = [System.Collections.ArrayList]::new()
$failed = [System.Collections.ArrayList]::new()

for ($i = 0; $i -lt $titles.Count; $i++) {
    $title = $titles[$i]
    $num = $i + 1
    $shortTitle = if ($title.Length -gt 65) { $title.Substring(0, 65) + "..." } else { $title }
    Log "[$num/$($titles.Count)] $shortTitle"

    $gotBib = $false
    $bibText = ""

    # ========== 方法1: DBLP ==========
    try {
        $encoded = [System.Uri]::EscapeDataString($title)
        $dblpUrl = "https://dblp.org/search/publ/api?q=$encoded&format=json&h=3"
        $dblpResp = Invoke-RestMethod -Uri $dblpUrl -Method Get -TimeoutSec 15 -ErrorAction Stop

        $hits = $null
        if ($dblpResp.result -and $dblpResp.result.hits) {
            $hits = $dblpResp.result.hits.hit
        }

        if ($hits -and $hits.Count -gt 0) {
            $info = $hits[0].info
            $bibUrl = "$($info.url.TrimEnd('/'))`.bib"

            $bibResp = Invoke-WebRequest -Uri $bibUrl -TimeoutSec 15 -UseBasicParsing -ErrorAction Stop
            if ($bibResp.Content -is [byte[]]) {
                $bibText = [System.Text.Encoding]::UTF8.GetString($bibResp.Content).Trim()
            } else {
                $bibText = "$($bibResp.Content)".Trim()
            }

            if ($bibText.Length -gt 30 -and $bibText -match '@') {
                $gotBib = $true
                $matchTitle = "$($info.title)".Substring(0, [Math]::Min(55, "$($info.title)".Length))
                Log "  DBLP: $matchTitle" Green
            }
        }

        if (-not $gotBib) {
            Log "  DBLP: no match" DarkYellow
        }
    } catch {
        Log "  DBLP: error" DarkYellow
    }

    # ========== 方法2: arXiv (fallback) ==========
    if (-not $gotBib) {
        Start-Sleep -Seconds 2
        try {
            # 用 ti: 前缀搜索每个关键词
            $words = ($title -replace '[^a-zA-Z0-9\s]', ' ') -split '\s+' | Where-Object { $_.Length -gt 2 }
            $queryParts = $words | ForEach-Object { "ti:$_" }
            $query = $queryParts -join '+AND+'
            $arxivUrl = "http://export.arxiv.org/api/query?search_query=$query&max_results=3&sortBy=relevance"

            $arxivResp = Invoke-WebRequest -Uri $arxivUrl -TimeoutSec 20 -UseBasicParsing -ErrorAction Stop
            if ($arxivResp.Content -is [byte[]]) {
                $xmlText = [System.Text.Encoding]::UTF8.GetString($arxivResp.Content)
            } else {
                $xmlText = "$($arxivResp.Content)"
            }

            # 手动解析 XML（避免命名空间问题）
            $entryPattern = '<entry>([\s\S]*?)</entry>'
            $entryMatches = [regex]::Matches($xmlText, $entryPattern)

            if ($entryMatches.Count -gt 0) {
                $entryXml = $entryMatches[0].Groups[1].Value

                # 提取字段
                $eTitle = if ($entryXml -match '<title>([\s\S]*?)</title>') { ($Matches[1] -replace '\s+', ' ').Trim() } else { $title }
                $eId = if ($entryXml -match '<id>https?://arxiv.org/abs/(.+?)</id>') { $Matches[1] } else { "" }
                $eYear = if ($entryXml -match '<published>(\d{4})') { $Matches[1] } else { "2025" }

                # 提取作者
                $authorMatches = [regex]::Matches($entryXml, '<name>(.+?)</name>')
                $authors = @()
                foreach ($am in $authorMatches) {
                    $authors += $am.Groups[1].Value
                }
                $authorStr = $authors -join ' and '
                $firstLast = if ($authors.Count -gt 0) { ($authors[0] -split ' ')[-1].ToLower() } else { "unknown" }

                # cite key
                $firstWord = ($eTitle -split '\s+')[0] -replace '[^a-zA-Z]', ''
                $citeKey = "${firstLast}${eYear}${firstWord}".ToLower()

                $bibText = "@article{$citeKey,`n  title     = {$eTitle},`n  author    = {$authorStr},`n  journal   = {arXiv preprint arXiv:$eId},`n  year      = {$eYear},`n  url       = {https://arxiv.org/abs/$eId}`n}"
                $gotBib = $true

                $matchShort = $eTitle.Substring(0, [Math]::Min(55, $eTitle.Length))
                Log "  arXiv: $matchShort" Cyan
            } else {
                Log "  arXiv: no entries found" DarkYellow
            }
        } catch {
            Log "  arXiv: error" DarkYellow
        }
    }

    # ========== 记录结果 ==========
    if ($gotBib) {
        [void]$results.Add("% Paper ${num}: $title`n$bibText")
    } else {
        [void]$failed.Add("${num}. $title")
        Log "  FAILED" Red
    }

    # arXiv 要求 3s 间隔
    Start-Sleep -Seconds 3
}

# ========== 写入输出 ==========
$header = "% Auto-generated BibTeX`n% Success: $($results.Count) / $($titles.Count)`n% Failed: $($failed.Count) / $($titles.Count)`n"
$body = $results -join "`n`n"
$content = "$header`n$body"

$outPath = Join-Path (Get-Location).Path $OutputFile
[System.IO.File]::WriteAllText($outPath, $content, [System.Text.Encoding]::UTF8)

Log ""
Log ("=" * 50) Cyan
Log "OK:   $($results.Count) / $($titles.Count)" Green
Log "FAIL: $($failed.Count) / $($titles.Count)" Red
Log "File: $outPath" Cyan

if ($failed.Count -gt 0) {
    Log ""
    Log "Failed list:" Red
    foreach ($f in $failed) {
        Log "  $f" Red
    }
}
