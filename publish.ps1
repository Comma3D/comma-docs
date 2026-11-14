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

function Get-GhIdentity {
    # Use the active `gh` account (lamlvo / teammate), not a shared Comma3D identity.
    $login = (gh api user -q .login 2>$null)
    if (-not $login) { throw "Not logged in to gh. Run: gh auth login (personal account with Write on $Repo)" }
    $id = (gh api user -q .id 2>$null)
    return @{
        Name  = $login
        Email = "$id+$login@users.noreply.github.com"
        Login = $login
    }
}

function Invoke-Git {
    param(
        [Parameter(Mandatory = $true)][string[]]$GitArgs,
        [hashtable]$Identity
    )
    & git -c "user.name=$($Identity.Name)" -c "user.email=$($Identity.Email)" @GitArgs
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
        throw "Could not create $Repo. Need admin on Comma3D (or ask an owner to create the repo)."
    }
}

$identity = Get-GhIdentity
Write-Host "Publishing as $($identity.Login) (active gh account)"

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
    if ($LASTEXITCODE -ne 0) { throw "Could not clone main. Check Write access on $Repo for $($identity.Login)." }
} else {
    New-Item -ItemType Directory -Force -Path $work | Out-Null
    Push-Location $work
    try {
        Invoke-Git -Identity $identity -GitArgs @("init", "-b", "main")
        Invoke-Git -Identity $identity -GitArgs @("remote", "add", "origin", $originUrl)
    }
    finally { Pop-Location }
}

Push-Location $work
try {
    Get-ChildItem -Force | Where-Object { $_.Name -ne ".git" } | Remove-Item -Recurse -Force

    $copy = @(
        "content", "layouts", "static", "assets", "hugo.yaml", ".gitignore",
        "README.md", ".github", "_build-content.ps1", "_gen_commands.py", "_changelog-user.md",
        "_publish-commarh-releases.ps1", "publish.ps1"
    )
    foreach ($name in $copy) {
        $from = Join-Path $SiteRoot $name
        if (Test-Path $from) {
            Copy-Item $from (Join-Path $work $name) -Recurse -Force
        }
    }

    Invoke-Git -Identity $identity -GitArgs @("add", "-A")
    $dirty = git status --porcelain
    if ($dirty) {
        Invoke-Git -Identity $identity -GitArgs @("commit", "-m", $message)
        if ($remoteHead) {
            Invoke-Git -Identity $identity -GitArgs @("push", "origin", "main")
        } else {
            Invoke-Git -Identity $identity -GitArgs @("push", "-u", "origin", "main")
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
