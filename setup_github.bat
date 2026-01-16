@echo off
REM Gold Price Calculator - GitHub Repository Setup for Windows
chcp 65001 >nul

echo 📦 Gold Price Calculator - GitHub Repository Setup
echo ==================================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git غير مثبت. الرجاء تثبيت Git أولاً:
    echo    https://git-scm.com/downloads
    pause
    exit /b 1
)

echo ✅ Git مثبت
echo.

REM Get GitHub username
set /p username="📝 أدخل اسم المستخدم على GitHub: "

if "%username%"=="" (
    echo ❌ اسم المستخدم مطلوب!
    pause
    exit /b 1
)

echo.
echo 🔧 جاري إعداد Repository...
echo.

REM Initialize Git
git init

REM Add all files
git add .

REM First commit
git commit -m "Initial commit: Gold Price Calculator with Web Scraping" -m "- حاسبة أسعار الذهب مع Web Scraping" -m "- جلب أسعار حية من saudigoldprice.com" -m "- Flask API Server" -m "- واجهة عربية احترافية" -m "- حساب تلقائي للمصنعية والضريبة"

REM Add remote
git remote add origin https://github.com/%username%/gold-price-calculator.git

REM Rename branch to main
git branch -M main

echo.
echo ✅ تم الإعداد بنجاح!
echo.
echo 📤 الآن قم برفع المشروع باستخدام:
echo    git push -u origin main
echo.
echo 🔗 رابط Repository:
echo    https://github.com/%username%/gold-price-calculator
echo.
echo 📚 لمزيد من التفاصيل، راجع SETUP_GUIDE.md
echo.
pause
