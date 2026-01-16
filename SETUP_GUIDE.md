# 📚 دليل رفع المشروع على GitHub

## 🎯 خطوات رفع المشروع

### الخطوة 1️⃣: إنشاء Repository على GitHub

1. اذهب إلى [GitHub](https://github.com)
2. اضغط على زر **"New"** أو **"+"** ثم **"New repository"**
3. املأ البيانات:
   - **Repository name**: `gold-price-calculator`
   - **Description**: `🏆 حاسبة أسعار الذهب مع Web Scraping | Gold Price Calculator with Web Scraping`
   - **Public** أو **Private**: اختر حسب رغبتك
   - ✅ أضف **README** (أو احذف هذا الخيار لأننا معنا README جاهز)
   - ❌ لا تضف **.gitignore** (معنا جاهز)
   - ✅ أضف **License**: MIT License
4. اضغط **"Create repository"**

### الخطوة 2️⃣: تجهيز المشروع محلياً

افتح Terminal (أو Command Prompt) في مجلد المشروع:

```bash
# انتقل لمجلد المشروع
cd /path/to/gold-price-calculator

# تهيئة Git
git init

# إضافة جميع الملفات
git add .

# عمل أول Commit
git commit -m "Initial commit: Gold Price Calculator with Web Scraping"
```

### الخطوة 3️⃣: ربط المشروع مع GitHub

```bash
# ربط المشروع مع Repository
git remote add origin https://github.com/YOUR-USERNAME/gold-price-calculator.git

# تغيير اسم Branch الرئيسي إلى main
git branch -M main

# رفع المشروع
git push -u origin main
```

**ملاحظة**: استبدل `YOUR-USERNAME` باسم المستخدم الخاص بك على GitHub

### الخطوة 4️⃣: إضافة Topics و About

في صفحة Repository على GitHub:

1. اضغط على ⚙️ بجانب **"About"**
2. أضف Topics:
   - `gold-price`
   - `web-scraping`
   - `flask`
   - `python`
   - `calculator`
   - `saudi-arabia`
   - `arabic`
3. أضف Website (إذا استضفت المشروع)
4. احفظ

## 🌟 تحسينات اختيارية

### إضافة GitHub Pages (لاستضافة الصفحة مجاناً)

1. في صفحة Repository، اذهب إلى **Settings**
2. في القائمة الجانبية، اضغط على **Pages**
3. في **Source**، اختر **main branch**
4. اضغط **Save**
5. بعد دقائق، الصفحة ستكون متاحة على:
   ```
   https://YOUR-USERNAME.github.io/gold-price-calculator/gold-calculator.html
   ```

**ملاحظة**: GitHub Pages يستضيف الصفحة الـ HTML فقط، السيرفر Python يحتاج استضافة منفصلة.

### إضافة Badge للـ README

أضف هذه Badges في أول README:

```markdown
![Stars](https://img.shields.io/github/stars/YOUR-USERNAME/gold-price-calculator?style=social)
![Forks](https://img.shields.io/github/forks/YOUR-USERNAME/gold-price-calculator?style=social)
![Issues](https://img.shields.io/github/issues/YOUR-USERNAME/gold-price-calculator)
![License](https://img.shields.io/github/license/YOUR-USERNAME/gold-price-calculator)
```

### إضافة Screenshot

1. خذ Screenshot من الصفحة
2. أنشئ مجلد `screenshots` في المشروع
3. احفظ الصورة فيه
4. أضف في README:
   ```markdown
   ## 📸 Screenshots
   
   ![Gold Calculator](screenshots/calculator.png)
   ```

## 🔄 التحديثات المستقبلية

عند تعديل الملفات:

```bash
# إضافة التغييرات
git add .

# عمل Commit
git commit -m "وصف التحديث"

# رفع التحديثات
git push origin main
```

## 🤝 السماح للآخرين بالمساهمة

### 1. إضافة ملف CONTRIBUTING.md

```markdown
# المساهمة في المشروع

نرحب بمساهماتك! اتبع هذه الخطوات:

1. Fork المشروع
2. أنشئ Branch جديد: `git checkout -b feature/amazing-feature`
3. Commit التغييرات: `git commit -m 'Add amazing feature'`
4. Push للـ Branch: `git push origin feature/amazing-feature`
5. افتح Pull Request
```

### 2. إضافة Issues Templates

في صفحة Repository:
1. اذهب إلى **Settings** > **Features**
2. فعّل **Issues**
3. أضف Issue Templates للـ Bug Reports و Feature Requests

## 📊 إضافة GitHub Actions (CI/CD)

لاختبار الكود تلقائياً، أنشئ `.github/workflows/test.yml`:

```yaml
name: Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    - name: Run tests
      run: |
        python -m pytest
```

## 🎉 جاهز!

مشروعك الآن على GitHub ويمكن للجميع رؤيته واستخدامه!

### 📱 شارك المشروع

شارك الرابط:
```
https://github.com/YOUR-USERNAME/gold-price-calculator
```

على:
- Twitter
- LinkedIn  
- Facebook
- WhatsApp
- المنتديات التقنية

---

## ❓ المساعدة

إذا واجهت أي مشكلة:
1. راجع [GitHub Docs](https://docs.github.com)
2. ابحث في Google عن الخطأ
3. اسأل في Stack Overflow

**بالتوفيق! 🚀**
