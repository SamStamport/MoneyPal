try {
    # Fetch latest remote refs quietly
    git fetch origin --quiet

    $local = (git rev-parse HEAD 2>$null).Trim()
    $origin = (git rev-parse origin/master 2>$null).Trim()
    $status = (git status --porcelain 2>$null)
    $modified = (git ls-files -m 2>$null) -join ';'
    $untracked = (git ls-files --others --exclude-standard 2>$null) -join ';'
    $lastFiles = git show --name-only --pretty=format:'%H %s' HEAD 2>$null
    $action = ''

    if ([string]::IsNullOrEmpty($status)) {
        if ($local -eq $origin) {
            $action = 'in-sync'
        } else {
            # If origin is an ancestor of local, push local -> origin
            git merge-base --is-ancestor origin/master HEAD 2>$null
            if ($LASTEXITCODE -eq 0) {
                git push origin master --quiet 2>$null
                if ($LASTEXITCODE -eq 0) { $action = 'pushed-local-to-origin' } else { $action = 'push-failed' }
            } else {
                $action = 'remote-ahead-or-diverged'
            }
        }
    } else {
        # Working tree has changes: stage, commit, push
        git add -A 2>$null
        $ts = Get-Date -Format 'yyyy-MM-dd_HH-mm-ss'
        git commit -m "backup (auto) $ts" --quiet 2>$null
        if ($LASTEXITCODE -eq 0) {
            git push origin master --quiet 2>$null
            if ($LASTEXITCODE -eq 0) { $action = 'committed-and-pushed' } else { $action = 'committed-but-push-failed' }
        } else {
            $action = 'commit-failed'
        }
    }

    $summary = @()
    $summary += "repo: $(Get-Location)"
    $summary += "local_head: $local"
    $summary += "origin_head: $origin"
    $summary += "status_porcelain: $status"
    $summary += "modified_tracked: $modified"
    $summary += "untracked: $untracked"
    $summary += "last_commit_files:"
    $summary += $lastFiles
    $summary += "action: $action"

    $summary | Out-File -FilePath backup_check.txt -Encoding UTF8
    exit 0
} catch {
    "ERROR: $_" | Out-File -FilePath backup_check.txt -Encoding UTF8
    exit 1
}