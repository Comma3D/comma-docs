# Push Hugo source to Comma3D/comma-docs (main). GitHub Actions builds Pages.
# -Deploy creates the repo if needed and pushes source. Does not upload a .yak.
param(
    [switch]$Deploy,
    [switch]$ContentOnly
)

$ErrorActionPreference = "Stop"
$SiteRoot = $PSScriptRoot
$Tools = Join-Path $SiteRoot ".tools"
$Hugo = Join-Path $Tools "hugo.exe"
$Theme = Join-Path $SiteRoot "themes\hextra"
$PublicDir = Join-Path $SiteRoot "public"
$Repo = "Comma3D/comma-docs"
$HugoVersion = "0.162.0"
$HextraRef = "v0.13.0"

function Ensure-Hugo {
    if (Test-Path $Hugo) { return }
    New-Item -ItemType Directory -Force -Path $Tools | Out-Null
    $zip = Join-Path $Tools "hugo.zip"
    $url = "https://github.com/gohugoio/hugo/releases/download/v$HugoVersion/hugo_extended_${HugoVersion}_windows-amd64.zip"
    Write-Host "Downloading Hugo $HugoVersion"
    curl.exe -fsSL $url -o $zip
    if ($LASTEXITCODE -ne 0) { throw "Could not download Hugo." }
    Expand-Archive -Path $zip -DestinationPath $Tools -Force
    Remove-Item $zip -Force
}

function Ensure-Theme {
    if (Test-Path (Join-Path $Theme "theme.toml")) { return }
    if (Test-Path $Theme) { Remove-Item $Theme -Recurse -Force }
    Write-Host "Cloning Hextra $HextraRef"
    git clone --depth 1 --branch $HextraRef https://github.com/imfing/hextra.git $Theme
    if ($LASTEXITCODE -ne 0) { throw "Could not clone Hextra." }
}

function Invoke-Git {
    param([Parameter(Mandatory = $true)][string[]]$GitArgs)
    & git -c user.name=Comma -c user.email=225508501+Comma3D@users.noreply.github.com @GitArgs
    if ($LASTEXITCODE -ne 0) { throw "git failed: git $($GitArgs -join ' ')" }
}

if (-not $ContentOnly) {
    $gen = Join-Path $SiteRoot "_build-content.ps1"
    if (Test-Path $gen) {
        & $gen
    }
}

Ensure-Hugo
Ensure-Theme

Push-Location $SiteRoot
try {
    & $Hugo --minify --gc
    if ($LASTEXITCODE -ne 0) { throw "Hugo build failed." }
}
finally {
    Pop-Location
}

Write-Host "Built $PublicDir"
if (-not $Deploy) {
    Write-Host "Local build only. Run publish.ps1 -Deploy to push source to $Repo."
    return
}

$prev = $ErrorActionPreference
$ErrorActionPreference = "Continue"
gh repo view $Repo --json name -q .name 1>$null 2>$null
$viewExit = $LASTEXITCODE
$ErrorActionPreference = $prev
if ($viewExit -ne 0) {
    Write-Host "Creating $Repo"
    $ErrorActionPreference = "Continue"
    gh repo create $Repo --public --description "Comma suite user guides (Rhino / Tekla / Revit). Source for https://comma3d.github.io/comma-docs/" --disable-wiki
    $createExit = $LASTEXITCODE
    $ErrorActionPreference = $prev
    if ($createExit -ne 0) {
        throw "Could not create $Repo. Switch gh to Comma3D and retry."
    }
}

$monorepo = Resolve-Path (Join-Path $SiteRoot "..\..")
$sha = (& git -C $monorepo.Path rev-parse --short HEAD).Trim()
$message = "Update docs (source commit $sha)"
$originUrl = "https://github.com/$Repo.git"
$work = Join-Path $env:TEMP "comma-docs-publish"
if (Test-Path $work) { Remove-Item $work -Recurse -Force }

$remoteHead = git ls-remote --heads $originUrl main
if ($LASTEXITCODE -ne 0) { throw "Could not read $originUrl." }

if ($remoteHead) {
    git clone --branch main --single-branch $originUrl $work
    if ($LASTEXITCODE -ne 0) { throw "Could not clone main." }
} else {
    New-Item -ItemType Directory -Force -Path $work | Out-Null
    Push-Location $work
    try {
        Invoke-Git -GitArgs @("init", "-b", "main")
        Invoke-Git -GitArgs @("remote", "add", "origin", $originUrl)
    }
    finally { Pop-Location }
}

Push-Location $work
try {
    Get-ChildItem -Force | Where-Object { $_.Name -ne ".git" } | Remove-Item -Recurse -Force

    $copy = @(
        "content", "layouts", "static", "assets", "hugo.yaml", ".gitignore",
        "README.md", ".github", "_build-content.ps1", "publish.ps1"
    )
    foreach ($name in $copy) {
        $from = Join-Path $SiteRoot $name
        if (Test-Path $from) {
            Copy-Item $from (Join-Path $work $name) -Recurse -Force
        }
    }

    Invoke-Git -GitArgs @("add", "-A")
    $dirty = git status --porcelain
    if ($dirty) {
        Invoke-Git -GitArgs @("commit", "-m", $message)
        if ($remoteHead) {
            Invoke-Git -GitArgs @("push", "origin", "main")
        } else {
            Invoke-Git -GitArgs @("push", "-u", "origin", "main")
        }
    } else {
        Write-Host "main is already current."
    }
}
finally {
    Pop-Location
}

# Prefer GitHub Actions Pages
$ErrorActionPreference = "Continue"
$pages = gh api "repos/$Repo/pages" 2>$null
$pagesExit = $LASTEXITCODE
$ErrorActionPreference = $prev
if ($pagesExit -ne 0) {
    Write-Host "Enabling GitHub Pages (Actions)"
    $body = '{"build_type":"workflow"}'
    $tmp = Join-Path $env:TEMP "comma-pages.json"
    [System.IO.File]::WriteAllText($tmp, $body)
    gh api --method POST "repos/$Repo/pages" --input $tmp
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Pages API create returned an error; enable Actions Pages in the repo Settings if the site 404s."
    }
}

Write-Host "Pushed source to https://github.com/$Repo"
Write-Host "Site: https://comma3d.github.io/comma-docs/"
