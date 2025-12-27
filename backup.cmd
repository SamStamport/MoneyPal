@echo off
echo ========================================
echo 🚀 STARTING BACKUP PROCESS...
echo ========================================

echo ✅ Step 1/3: Staging all changes...
git add .
if %errorlevel% neq 0 (
    echo ❌ ERROR: Failed to stage changes
    pause
    exit /b 1
)
echo    ✓ All changes staged successfully

echo ✅ Step 2/3: Committing changes...
git commit -m "Backup: %date% %time%"
if %errorlevel% neq 0 (
    echo ❌ ERROR: Failed to commit changes
    pause
    exit /b 1
)
echo    ✓ Changes committed successfully

echo ✅ Step 3/3: Pushing to GitHub...
for /f "tokens=*" %%i in ('git branch --show-current') do set BRANCH=%%i
if "%BRANCH%"=="" (
    echo ❌ ERROR: Could not detect current branch
    pause
    exit /b 1
)
echo    Current branch: %BRANCH%
git push origin %BRANCH%
if %errorlevel% neq 0 (
    echo ❌ ERROR: Failed to push to GitHub
    pause
    exit /b 1
)
echo    ✓ Successfully pushed to GitHub

echo ========================================
echo 🎉 BACKUP COMPLETE! All steps finished.
echo ========================================