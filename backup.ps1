Write-Host "========================================" -ForegroundColor Cyan
Write-Host "🚀 STARTING BACKUP PROCESS..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "✅ Step 1/3: Staging all changes..." -ForegroundColor Green
git add .
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ ERROR: Failed to stage changes" -ForegroundColor Red
    Read-Host "Press Enter to continue"
    exit 1
}
Write-Host "   ✓ All changes staged successfully" -ForegroundColor Green
Write-Host ""

Write-Host "✅ Step 2/3: Committing changes..." -ForegroundColor Green
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
git commit -m "Backup: $timestamp"
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ ERROR: Failed to commit changes" -ForegroundColor Red
    Read-Host "Press Enter to continue"
    exit 1
}
Write-Host "   ✓ Changes committed successfully" -ForegroundColor Green
Write-Host ""

Write-Host "✅ Step 3/3: Pushing to GitHub..." -ForegroundColor Green
git push origin main
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ ERROR: Failed to push to GitHub" -ForegroundColor Red
    Read-Host "Press Enter to continue"
    exit 1
}
Write-Host "   ✓ Successfully pushed to GitHub" -ForegroundColor Green
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "🎉 BACKUP COMPLETE! All steps finished." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan