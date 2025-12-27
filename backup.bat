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
if %errorlevel% equ 1 (
    echo    ℹ️ Nothing to commit - working tree clean
    goto push
)
if %errorlevel% neq 0 (
    echo ❌ ERROR: Failed to commit changes
    pause
    exit /b 1
)
echo    ✓ Changes committed successfully

:push

echo ✅ Step 3/3: Pushing to GitHub...
echo    Pushing to master branch...
git push origin master
if %errorlevel% neq 0 (
    echo ❌ ERROR: Failed to push to GitHub
    pause
    exit /b 1
)
echo    ✓ Successfully pushed to GitHub

echo ========================================
echo 🎉 BACKUP COMPLETE! All steps finished.
echo ========================================