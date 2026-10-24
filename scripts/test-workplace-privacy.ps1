param([switch]$Published)
$ErrorActionPreference = 'Stop'
$root = Split-Path $PSScriptRoot
$languages = @(Get-Content "$root/_data/workplace_privacy_languages.json" -Raw | ConvertFrom-Json)
if ($languages.Count -ne 18 -or @($languages.tag | Sort-Object -Unique).Count -ne 18) { throw 'Expected 18 policy locales' }
$expected = @('en','ko','ja','zh-Hans','zh-Hant','vi','id','ne','km','my','th','uz','mn','si','lo','bn','ur','hi')
$layout = Get-Content "$root/_layouts/workplace-korean.html" -Raw
if ($layout -notmatch 'page.text_direction' -or $layout -match 'page.dir' -or $layout -notmatch 'site.data.workplace_privacy_languages') { throw 'Missing RTL/navigation or reserved Jekyll dir field used' }
foreach ($tag in $expected) {
    $entry = $languages | Where-Object tag -eq $tag
    if (-not $entry) { throw "Missing locale $tag" }
    $file = Join-Path $root ($entry.path.TrimStart('/') + 'index.md')
    $body = Get-Content -LiteralPath $file -Raw
    if ($body -notmatch "(?m)^lang: $([regex]::Escape($tag))\s*$") { throw "$tag front matter mismatch" }
    if ([regex]::Matches($body, '(?m)^## [1-9]\. ').Count -ne 9) { throw "$tag section count" }
    foreach ($token in @('Workplace Korean','com.minororbit.workplacekorean','davidleepub@gmail.com','MP3','TTS','Google','Unity','UMP','TLS','DataStore','GitHub','fal.ai','ElevenLabs','Acquire Optimization','4.16.6','25.5.0')) {
        if (-not $body.Contains($token)) { throw "$tag missing disclosure anchor: $token" }
    }
    if ($body.Contains([char]0xFFFD) -or $body -match 'TODO|PLACEHOLDER') { throw "$tag damaged/incomplete text" }
    if ($tag -eq 'ur' -and $body -notmatch '(?m)^text_direction: rtl\s*$') { throw 'Urdu must use RTL' }
    if ($Published) {
        $url = 'https://minor-orbit.github.io/medical-chinese-legal' + $entry.path
        $response = Invoke-WebRequest $url -TimeoutSec 30
        $direction = if ($tag -eq 'ur') { 'rtl' } else { 'ltr' }
        if ($response.StatusCode -ne 200 -or $response.Content -notmatch ('<html lang="' + [regex]::Escape($tag) + '" dir="' + $direction + '">')) { throw "$tag live locale/direction failure" }
        if ([regex]::Matches($response.Content, 'hreflang=').Count -ne 18 -or [regex]::Matches($response.Content, '<h2').Count -ne 9) { throw "$tag live navigation/sections failure" }
        "LIVE PASS $tag"
    }
}
'PASS: 18 policy locales; 9 sections each; disclosure anchors; language navigation; Urdu RTL.'
