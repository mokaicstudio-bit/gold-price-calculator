#!/bin/bash
# 🚀 Quick Start Script for GitHub Repository

echo "📦 Gold Price Calculator - GitHub Repository Setup"
echo "=================================================="
echo ""

# تحقق من وجود git
if ! command -v git &> /dev/null; then
    echo "❌ Git غير مثبت. الرجاء تثبيت Git أولاً:"
    echo "   https://git-scm.com/downloads"
    exit 1
fi

echo "✅ Git مثبت"
echo ""

# اطلب اسم المستخدم
read -p "📝 أدخل اسم المستخدم على GitHub: " username

if [ -z "$username" ]; then
    echo "❌ اسم المستخدم مطلوب!"
    exit 1
fi

echo ""
echo "🔧 جاري إعداد Repository..."
echo ""

# تهيئة Git
git init

# إضافة جميع الملفات
git add .

# أول Commit
git commit -m "Initial commit: Gold Price Calculator with Web Scraping

- حاسبة أسعار الذهب مع Web Scraping
- جلب أسعار حية من saudigoldprice.com
- Flask API Server
- واجهة عربية احترافية
- حساب تلقائي للمصنعية والضريبة"

# ربط مع GitHub
git remote add origin "https://github.com/$username/gold-price-calculator.git"

# تغيير Branch لـ main
git branch -M main

echo ""
echo "✅ تم الإعداد بنجاح!"
echo ""
echo "📤 الآن قم برفع المشروع باستخدام:"
echo "   git push -u origin main"
echo ""
echo "🔗 رابط Repository:"
echo "   https://github.com/$username/gold-price-calculator"
echo ""
echo "📚 لمزيد من التفاصيل، راجع SETUP_GUIDE.md"
echo ""
