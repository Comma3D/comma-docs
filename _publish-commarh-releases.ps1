# Create GitHub Releases CommaRh-v26.* on the PUBLIC docs repo from CommaRh/CHANGELOG.md.
# Comma3D/Comma is private — releases there 404 for the public. Use comma-docs instead.
# Only the current Package Manager line (26.x). Does NOT create Issues.
# Safe to re-run (skips tags that already exist).
param(
    [string]$Repo = "Comma3D/comma-docs",
    [string]$ChangelogPath = "",
    [string]$VersionPrefix = "26."
)

$ErrorActionPreference = "Stop"
if (-not $ChangelogPath) {
    $ChangelogPath = Join-Path $PSScriptRoot "_changelog-user.md"
}
if (-not (Test-Path $ChangelogPath)) { throw "CHANGELOG not found: $ChangelogPath" }

$text = [System.IO.File]::ReadAllText($ChangelogPath)
$rx = [regex]::new('(?ms)^## \[([^\]]+)\] - (\d{4}-\d{2}-\d{2})\s*\r?\n(.*?)(?=^## \[|\z)')
$matches = @($rx.Matches($text))
if ($matches.Count -eq 0) { throw "No version sections found in CHANGELOG." }

# Oldest first so the newest can be marked Latest
$entries = foreach ($m in $matches) {
    $ver = $m.Groups[1].Value.Trim()
    if (-not $ver.StartsWith($VersionPrefix)) { continue }
    # Require Major.Minor.Patch (skip odd historical labels)
    if ($ver -notmatch '^\d+\.\d+\.\d+$') { continue }
    [pscustomobject]@{
        Version = $ver
        Date    = $m.Groups[2].Value.Trim()
        Body    = $m.Groups[3].Value.Trim()
    }
}
$entries = @($entries | Sort-Object {
    $p = $_.Version -split '\.'
    [int64]$p[0] * 1000000L + [int64]$p[1] * 1000L + [int64]$p[2]
})
if ($entries.Count -eq 0) { throw "No CHANGELOG sections match prefix '$VersionPrefix'." }
Write-Host "Will publish $($entries.Count) releases: $($entries.Version -join ', ')"

$existing = @(gh release list --repo $Repo --limit 200 --json tagName -q ".[].tagName" 2>$null)
if (-not $existing) { $existing = @() }

foreach ($e in $entries) {
    $tag = "CommaRh-v$($e.Version)"
    if ($existing -contains $tag) {
        Write-Host "Skip existing $tag"
        continue
    }

    $notes = @"
## CommaRh $($e.Version) — $($e.Date)

Install from the Rhino 8 Package Manager: search **CommaRh**.

Docs: https://comma3d.github.io/comma-docs/rhino/
Changelog: https://comma3d.github.io/comma-docs/rhino/docs/getting-started/changelog/

$($e.Body)
"@
    $tmp = Join-Path $env:TEMP "commarh-release-$($e.Version).md"
    [System.IO.File]::WriteAllText($tmp, $notes)

    # Only the newest 26.x release is "Latest" on the public docs repo.
    $isLatest = ($e.Version -eq $entries[-1].Version)
    $ghArgs = @(
        "release", "create", $tag,
        "--repo", $Repo,
        "--title", "CommaRh $($e.Version)",
        "--notes-file", $tmp
    )
    if (-not $isLatest) { $ghArgs += "--latest=false" }

    Write-Host "Creating $tag ..."
    & gh @ghArgs
    if ($LASTEXITCODE -ne 0) { throw "gh release create failed for $tag" }
}

Write-Host "Done. Releases: https://github.com/$Repo/releases?q=CommaRh"
