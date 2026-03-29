<#
.SYNOPSIS
  Search academic papers for an agent via Semantic Scholar API.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$Query,

    [ValidateRange(1, 500)]
    [int]$TopK = 10,

    [Nullable[int]]$YearFrom = $null,
    [Nullable[int]]$YearTo = $null,

    [switch]$OpenAccessOnly,

    [ValidateRange(0, 10000000)]
    [int]$MinCitationCount = 0,

    [string]$FieldsOfStudy,
    [string]$Venue,

    [ValidateSet("relevance", "latest", "citations")]
    [string]$SortBy = "relevance",

    [ValidateSet("json", "object", "table")]
    [string]$Output = "json",

    [string]$ApiKey = $env:S2_API_KEY,

    [ValidateRange(5, 300)]
    [int]$TimeoutSec = 30,

    [ValidateRange(0, 10)]
    [int]$MaxRetries = 2
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

try {
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
} catch {
}

function New-QueryString {
    param(
        [Parameter(Mandatory = $true)]
        [hashtable]$Params
    )

    $pairs = New-Object System.Collections.Generic.List[string]

    foreach ($key in $Params.Keys) {
        $value = $Params[$key]
        if ($null -eq $value) { continue }

        $encodedKey = [uri]::EscapeDataString([string]$key)

        if ($value -is [System.Management.Automation.SwitchParameter]) {
            if ($value.IsPresent) {
                $pairs.Add($encodedKey)
            }
            continue
        }

        if ($value -is [bool]) {
            $pairs.Add(("{0}={1}" -f $encodedKey, ([string]$value).ToLowerInvariant()))
            continue
        }

        $pairs.Add(("{0}={1}" -f $encodedKey, [uri]::EscapeDataString([string]$value)))
    }

    return ($pairs -join "&")
}

function ConvertTo-YearFilter {
    param(
        $From,
        $To
    )

    $hasFrom = ($null -ne $From -and [string]$From -ne "")
    $hasTo   = ($null -ne $To   -and [string]$To   -ne "")

    if ($hasFrom -and $hasTo) {
        return "{0}-{1}" -f [int]$From, [int]$To
    }
    elseif ($hasFrom) {
        return "{0}-" -f [int]$From
    }
    elseif ($hasTo) {
        return "-{0}" -f [int]$To
    }
    else {
        return $null
    }
}

function Get-ResponseBodyFromException {
    param(
        [Parameter(Mandatory = $true)]
        $Exception
    )

    $body = $null

    try {
        if ($Exception.Response -and $Exception.Response.GetResponseStream) {
            $stream = $Exception.Response.GetResponseStream()
            if ($stream) {
                $reader = New-Object System.IO.StreamReader($stream)
                try {
                    $body = $reader.ReadToEnd()
                } finally {
                    $reader.Close()
                }
            }
        }
    } catch {
    }

    return $body
}

function Get-HttpStatusCodeFromException {
    param(
        [Parameter(Mandatory = $true)]
        $Exception
    )

    try {
        if ($Exception.Response -and $Exception.Response.StatusCode) {
            return [int]$Exception.Response.StatusCode
        }
    } catch {
    }

    return $null
}

function Get-HttpStatusDescriptionFromException {
    param(
        [Parameter(Mandatory = $true)]
        $Exception
    )

    try {
        if ($Exception.Response -and $Exception.Response.StatusDescription) {
            return [string]$Exception.Response.StatusDescription
        }
    } catch {
    }

    return $null
}

function Invoke-S2Request {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Uri,

        [Parameter(Mandatory = $true)]
        [hashtable]$Headers,

        [int]$TimeoutSec = 30,

        [int]$MaxRetries = 2
    )

    $attempt = 0

    while ($true) {
        try {
            return Invoke-RestMethod -Method GET -Uri $Uri -Headers $Headers -TimeoutSec $TimeoutSec
        }
        catch {
            $attempt++
            $statusCode = Get-HttpStatusCodeFromException -Exception $_.Exception
            $statusDesc = Get-HttpStatusDescriptionFromException -Exception $_.Exception
            $body = Get-ResponseBodyFromException -Exception $_.Exception
            $rawMessage = $_.Exception.Message

            $shouldRetry = $false
            if ($attempt -le $MaxRetries) {
                if ($statusCode -in @(429, 500, 502, 503, 504) -or $null -eq $statusCode) {
                    $shouldRetry = $true
                }
            }

            if ($shouldRetry) {
                $sleepSeconds = [Math]::Min(10, [Math]::Pow(2, $attempt))
                Start-Sleep -Seconds $sleepSeconds
                continue
            }

            $parts = @()
            $parts += "Semantic Scholar API request failed."
            $parts += "URI: $Uri"

            if ($null -ne $statusCode) {
                $parts += "HTTP: $statusCode $statusDesc"
            }

            if (-not [string]::IsNullOrWhiteSpace($body)) {
                $parts += "Body: $body"
            } else {
                $parts += "Message: $rawMessage"
            }

            throw ($parts -join "`n")
        }
    }
}

function Get-AuthorsString {
    param($Authors)

    if ($null -eq $Authors) { return "" }

    $names = New-Object System.Collections.Generic.List[string]
    foreach ($a in $Authors) {
        if ($null -ne $a) {
            if ($a.PSObject.Properties.Name -contains "name") {
                if (-not [string]::IsNullOrWhiteSpace([string]$a.name)) {
                    [void]$names.Add([string]$a.name)
                }
            }
        }
    }

    return ($names -join ", ")
}

function Get-ExternalIdValue {
    param(
        $ExternalIds,
        [string]$Key
    )

    if ($null -eq $ExternalIds) { return $null }
    if (-not ($ExternalIds.PSObject.Properties.Name -contains $Key)) { return $null }

    $value = $ExternalIds.$Key
    if ($null -eq $value) { return $null }

    if ($value -is [System.Array]) {
        if ($value.Count -gt 0) {
            return ($value -join ",")
        }
        return $null
    }

    return [string]$value
}

function Get-OpenAccessPdfUrl {
    param($Paper)

    if ($null -eq $Paper) { return $null }
    if (-not ($Paper.PSObject.Properties.Name -contains "openAccessPdf")) { return $null }
    if ($null -eq $Paper.openAccessPdf) { return $null }

    if ($Paper.openAccessPdf.PSObject.Properties.Name -contains "url") {
        return $Paper.openAccessPdf.url
    }

    return $null
}

function Get-FieldsOfStudyList {
    param($Paper)

    if ($null -eq $Paper) { return @() }
    if (-not ($Paper.PSObject.Properties.Name -contains "fieldsOfStudy")) { return @() }
    if ($null -eq $Paper.fieldsOfStudy) { return @() }

    $vals = @()
    foreach ($x in $Paper.fieldsOfStudy) {
        if ($null -ne $x -and -not [string]::IsNullOrWhiteSpace([string]$x)) {
            $vals += [string]$x
        }
    }
    return $vals
}

function Normalize-Paper {
    param($Paper)

    $paperId = $null
    if ($Paper.PSObject.Properties.Name -contains "paperId") { $paperId = $Paper.paperId }

    $title = $null
    if ($Paper.PSObject.Properties.Name -contains "title") { $title = $Paper.title }

    $year = $null
    if ($Paper.PSObject.Properties.Name -contains "year") { $year = $Paper.year }

    $publicationDate = $null
    if ($Paper.PSObject.Properties.Name -contains "publicationDate") { $publicationDate = $Paper.publicationDate }

    $citationCount = 0
    if ($Paper.PSObject.Properties.Name -contains "citationCount" -and $null -ne $Paper.citationCount) {
        $citationCount = [int]$Paper.citationCount
    }

    $venueValue = $null
    if ($Paper.PSObject.Properties.Name -contains "venue") { $venueValue = $Paper.venue }

    $url = $null
    if ($Paper.PSObject.Properties.Name -contains "url") { $url = $Paper.url }

    $abstract = $null
    if ($Paper.PSObject.Properties.Name -contains "abstract") { $abstract = $Paper.abstract }

    $isOpenAccess = $false
    if ($Paper.PSObject.Properties.Name -contains "isOpenAccess" -and $null -ne $Paper.isOpenAccess) {
        $isOpenAccess = [bool]$Paper.isOpenAccess
    }

    $fields = Get-FieldsOfStudyList -Paper $Paper

    [PSCustomObject]@{
        id              = $paperId
        title           = $title
        year            = $year
        publicationDate = $publicationDate
        citationCount   = $citationCount
        venue           = $venueValue
        authors         = Get-AuthorsString -Authors $Paper.authors
        fieldsOfStudy   = $fields
        url             = $url
        doi             = Get-ExternalIdValue -ExternalIds $Paper.externalIds -Key "DOI"
        arxivId         = Get-ExternalIdValue -ExternalIds $Paper.externalIds -Key "ArXiv"
        corpusId        = Get-ExternalIdValue -ExternalIds $Paper.externalIds -Key "CorpusId"
        isOpenAccess    = $isOpenAccess
        pdfUrl          = Get-OpenAccessPdfUrl -Paper $Paper
        abstract        = $abstract
    }
}

function Test-PaperMatchesLocalFilters {
    param(
        [Parameter(Mandatory = $true)]
        $Paper,

        [switch]$OpenAccessOnly,

        [int]$MinCitationCount = 0,

        [string]$FieldsOfStudy,

        [string]$Venue
    )

    if ($OpenAccessOnly) {
        $hasOpen = $false
        if ($Paper.isOpenAccess -eq $true) { $hasOpen = $true }
        if (-not $hasOpen -and -not [string]::IsNullOrWhiteSpace([string]$Paper.pdfUrl)) { $hasOpen = $true }
        if (-not $hasOpen) { return $false }
    }

    if ($Paper.citationCount -lt $MinCitationCount) {
        return $false
    }

    if (-not [string]::IsNullOrWhiteSpace($Venue)) {
        $paperVenue = [string]$Paper.venue
        if ([string]::IsNullOrWhiteSpace($paperVenue)) { return $false }
        if ($paperVenue -notlike ("*" + $Venue + "*")) { return $false }
    }

    if (-not [string]::IsNullOrWhiteSpace($FieldsOfStudy)) {
        $wanted = $FieldsOfStudy.Split(",") | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne "" }
        $paperFields = @($Paper.fieldsOfStudy)

        if ($paperFields.Count -eq 0) { return $false }

        $matched = $false
        foreach ($wf in $wanted) {
            foreach ($pf in $paperFields) {
                if ([string]$pf -like ("*" + $wf + "*")) {
                    $matched = $true
                    break
                }
            }
            if ($matched) { break }
        }

        if (-not $matched) { return $false }
    }

    return $true
}

function Search-SemanticScholarRelevance {
    param(
        [string]$Query,
        [int]$TopK,
        [string]$YearFilter,
        [switch]$OpenAccessOnly,
        [int]$MinCitationCount,
        [string]$FieldsOfStudy,
        [string]$Venue,
        [hashtable]$Headers,
        [int]$TimeoutSec,
        [int]$MaxRetries
    )

    $baseUrl = "https://api.semanticscholar.org/graph/v1/paper/search"
    $fields = "paperId,title,abstract,year,publicationDate,citationCount,authors,venue,url,externalIds,openAccessPdf,isOpenAccess,fieldsOfStudy"

    $results = New-Object System.Collections.Generic.List[object]
    $seenIds = @{}
    $offset = 0
    $maxIterations = 20
    $iteration = 0

    while ($results.Count -lt $TopK -and $iteration -lt $maxIterations) {
        $iteration++
        $pageSize = 100

        $params = @{
            query  = $Query
            offset = $offset
            limit  = $pageSize
            fields = $fields
        }

        if (-not [string]::IsNullOrWhiteSpace($YearFilter)) {
            $params["year"] = $YearFilter
        }

        $uri = "{0}?{1}" -f $baseUrl, (New-QueryString -Params $params)
        $resp = Invoke-S2Request -Uri $uri -Headers $Headers -TimeoutSec $TimeoutSec -MaxRetries $MaxRetries

        if ($null -eq $resp -or $null -eq $resp.data -or $resp.data.Count -eq 0) {
            break
        }

        foreach ($rawPaper in $resp.data) {
            $paper = Normalize-Paper -Paper $rawPaper
            $paperId = [string]$paper.id

            if ([string]::IsNullOrWhiteSpace($paperId)) {
                $paperId = [string]$paper.title
            }

            if ($seenIds.ContainsKey($paperId)) {
                continue
            }

            $seenIds[$paperId] = $true

            if (Test-PaperMatchesLocalFilters -Paper $paper -OpenAccessOnly:$OpenAccessOnly -MinCitationCount $MinCitationCount -FieldsOfStudy $FieldsOfStudy -Venue $Venue) {
                [void]$results.Add($paper)
                if ($results.Count -ge $TopK) { break }
            }
        }

        if ($resp.PSObject.Properties.Name -contains "next" -and $null -ne $resp.next) {
            $offset = [int]$resp.next
        }
        else {
            break
        }
    }

    return $results
}

function Search-SemanticScholarBulk {
    param(
        [string]$Query,
        [int]$TopK,
        [string]$YearFilter,
        [switch]$OpenAccessOnly,
        [int]$MinCitationCount,
        [string]$FieldsOfStudy,
        [string]$Venue,
        [string]$SortBy,
        [hashtable]$Headers,
        [int]$TimeoutSec,
        [int]$MaxRetries
    )

    $baseUrl = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
    $fields = "paperId,title,abstract,year,publicationDate,citationCount,authors,venue,url,externalIds,openAccessPdf,isOpenAccess,fieldsOfStudy"

    $sort = switch ($SortBy) {
        "latest"    { "publicationDate:desc" }
        "citations" { "citationCount:desc" }
        default     { "publicationDate:desc" }
    }

    $results = New-Object System.Collections.Generic.List[object]
    $seenIds = @{}
    $token = $null
    $maxIterations = 20
    $iteration = 0

    while ($results.Count -lt $TopK -and $iteration -lt $maxIterations) {
        $iteration++
        $pageSize = 100

        $params = @{
            query  = $Query
            limit  = $pageSize
            fields = $fields
            sort   = $sort
        }

        if (-not [string]::IsNullOrWhiteSpace($YearFilter)) {
            $params["year"] = $YearFilter
        }

        if (-not [string]::IsNullOrWhiteSpace($token)) {
            $params["token"] = $token
        }

        $uri = "{0}?{1}" -f $baseUrl, (New-QueryString -Params $params)
        $resp = Invoke-S2Request -Uri $uri -Headers $Headers -TimeoutSec $TimeoutSec -MaxRetries $MaxRetries

        if ($null -eq $resp -or $null -eq $resp.data -or $resp.data.Count -eq 0) {
            break
        }

        foreach ($rawPaper in $resp.data) {
            $paper = Normalize-Paper -Paper $rawPaper
            $paperId = [string]$paper.id

            if ([string]::IsNullOrWhiteSpace($paperId)) {
                $paperId = [string]$paper.title
            }

            if ($seenIds.ContainsKey($paperId)) {
                continue
            }

            $seenIds[$paperId] = $true

            if (Test-PaperMatchesLocalFilters -Paper $paper -OpenAccessOnly:$OpenAccessOnly -MinCitationCount $MinCitationCount -FieldsOfStudy $FieldsOfStudy -Venue $Venue) {
                [void]$results.Add($paper)
                if ($results.Count -ge $TopK) { break }
            }
        }

        if ($resp.PSObject.Properties.Name -contains "token" -and -not [string]::IsNullOrWhiteSpace([string]$resp.token)) {
            $token = [string]$resp.token
        }
        else {
            break
        }
    }

    return $results
}

function Format-Output {
    param(
        [Parameter(Mandatory = $true)]
        [System.Collections.IEnumerable]$Papers,

        [ValidateSet("json", "object", "table")]
        [string]$Output
    )

    switch ($Output) {
        "object" {
            return $Papers
        }
        "table" {
            $Papers |
                Select-Object year, publicationDate, citationCount, title, authors, venue, doi, pdfUrl, url |
                Format-Table -AutoSize
            return
        }
        default {
            $Papers | ConvertTo-Json -Depth 8
            return
        }
    }
}

$headers = @{
    "Accept"     = "application/json"
    "User-Agent" = "PaperAgent/1.0 (PowerShell)"
}

if (-not [string]::IsNullOrWhiteSpace($ApiKey)) {
    $headers["x-api-key"] = $ApiKey
}

$yearFilter = ConvertTo-YearFilter -From $YearFrom -To $YearTo

$papers =
    if ($SortBy -eq "relevance") {
        Search-SemanticScholarRelevance `
            -Query $Query `
            -TopK $TopK `
            -YearFilter $yearFilter `
            -OpenAccessOnly:$OpenAccessOnly `
            -MinCitationCount $MinCitationCount `
            -FieldsOfStudy $FieldsOfStudy `
            -Venue $Venue `
            -Headers $headers `
            -TimeoutSec $TimeoutSec `
            -MaxRetries $MaxRetries
    }
    else {
        Search-SemanticScholarBulk `
            -Query $Query `
            -TopK $TopK `
            -YearFilter $yearFilter `
            -OpenAccessOnly:$OpenAccessOnly `
            -MinCitationCount $MinCitationCount `
            -FieldsOfStudy $FieldsOfStudy `
            -Venue $Venue `
            -SortBy $SortBy `
            -Headers $headers `
            -TimeoutSec $TimeoutSec `
            -MaxRetries $MaxRetries
    }

Format-Output -Papers $papers -Output $Output