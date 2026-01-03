Param(
    [switch]$CreateRemote = $false,
    [ValidateSet("public","private")][string]$Visibility = "public"
)

$repoDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Push-Location $repoDir

Write-Host "Running backup script in: $repoDir"

if (!(Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: 'git' is not installed or not in PATH. Install git and try again." -ForegroundColor Red
    Pop-Location
    exit 1
}

if (!(Test-Path .git)) {
    git init
    Write-Host "Initialized local git repository."
} else {
    Write-Host "Git repository already initialized."
}

# Ensure there's some user identity set locally (fall back to global if available)
$localName = git config user.name 2>$null
$localEmail = git config user.email 2>$null
if (-not $localName) {
    $globalName = git config --global user.name 2>$null
    if ($globalName) { git config user.name $globalName }
}
if (-not $localEmail) {
    $globalEmail = git config --global user.email 2>$null
    if ($globalEmail) { git config user.email $globalEmail }
}

git add -A
$status = git status --porcelain
if ($status) {
    git commit -m "Backup: commit $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    Write-Host "Committed changes to local repo."
} else {
    Write-Host "No changes to commit."
}

if ($CreateRemote) {
    if (!(Get-Command gh -ErrorAction SilentlyContinue)) {
        Write-Host "WARNING: GitHub CLI 'gh' not found. Install it and run 'gh auth login' to enable creating/pushing remotes." -ForegroundColor Yellow
    } else {
        $remotes = git remote
        if ($remotes) {
            Write-Host "Remote(s) already configured: $remotes"
        } else {
            $repoName = Split-Path -Leaf (Get-Location)
            Write-Host "Creating GitHub repository '$repoName' (visibility: $Visibility) and pushing..."
            gh repo create $repoName --$Visibility --source=. --push --confirm
            if ($LASTEXITCODE -eq 0) {
                Write-Host "Remote created and pushed successfully."
            } else {
                Write-Host "Failed to create/push remote repo. gh exit code: $LASTEXITCODE" -ForegroundColor Red
            }
        }
    }
} else {
    Write-Host "Skipping remote creation. Re-run with -CreateRemote to attempt pushing to GitHub (requires 'gh' and login)."
}

Pop-Location
