# After a CommaRh Yak ship: refresh public docs + create CommaRh-v* release notes.
# Run as a personal GitHub account with Write on Comma3D/comma-docs (e.g. lamlvo).
# Does NOT upload Yak. Does NOT touch private Comma3D/Comma releases.
param(
    [switch]$SkipDeploy,
    [switch]$SkipRelease,
    [switch]$ContentOnly
)

$ErrorActionPreference = "Stop"
$Root = $PSScriptRoot

Push-Location $Root
try {
    Write-Host "=== 1/3 Build content (_build-content / changelog user) ==="
    & (Join-Path $Root "_build-content.ps1")
    if ($LASTEXITCODE -ne 0) { throw "_build-content.ps1 failed." }

    if (-not $SkipDeploy) {
        Write-Host "=== 2/3 Deploy Pages (publish.ps1 -Deploy) ==="
        $pubArgs = @("-Deploy")
        if ($ContentOnly) { $pubArgs += "-ContentOnly" }
        & (Join-Path $Root "publish.ps1") @pubArgs
        if ($LASTEXITCODE -ne 0) { throw "publish.ps1 failed." }
    } else {
        Write-Host "=== 2/3 Deploy skipped (-SkipDeploy) ==="
    }

    if (-not $SkipRelease) {
        Write-Host "=== 3/3 GitHub Releases on Comma3D/comma-docs ==="
        & (Join-Path $Root "_publish-commarh-releases.ps1")
        if ($LASTEXITCODE -ne 0) { throw "_publish-commarh-releases.ps1 failed." }
    } else {
        Write-Host "=== 3/3 Releases skipped (-SkipRelease) ==="
    }
}
finally {
    Pop-Location
}

Write-Host ""
Write-Host "Docs:      https://comma3d.github.io/comma-docs/rhino/"
Write-Host "Changelog: https://comma3d.github.io/comma-docs/rhino/docs/getting-started/changelog/"
Write-Host "Releases:  https://github.com/Comma3D/comma-docs/releases"
