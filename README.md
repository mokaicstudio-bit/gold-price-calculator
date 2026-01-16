# 💰 حاسبة أسعار الذهب | Gold Price Calculator

<div align="center">

![Gold](https://img.shields.io/badge/Gold-Price-FFD700?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

**حاسبة احترافية لأسعار الذهب مع Web Scraping من saudigoldprice.com**

[العربية](#-النسخة-العربية) | [English](#-english-version)

</div>

---

## 🌟 النسخة العربية

### 📋 نظرة عامة

حاسبة أسعار الذهب هي أداة متكاملة تتيح لك:
- 📊 جلب أسعار الذهب الحية من saudigoldprice.com
- 🔄 تحديث تلقائي كل 5 دقائق
- 💎 حساب قيمة الحلي، السبائك، والجنيهات
- 💰 حساب المصنعية تلقائياً
- 📈 حساب الضريبة 15%
- 🎨 واجهة عربية احترافية

### ✨ المميزات

- ✅ **Web Scraping حقيقي**: يجلب الأسعار مباشرة من saudigoldprice.com
- ✅ **تحديث تلقائي**: الأسعار تتحدث كل 5 دقائق
- ✅ **حساب ذكي**: يحسب المصنعية والضريبة تلقائياً
- ✅ **دعم شامل**: حلي (عيار 24،22،21،18،14)، سبائك (1جم - 1كجم)، جنيهات
- ✅ **تصميم احترافي**: واجهة عربية جميلة ومتجاوبة
- ✅ **API مفتوح**: يمكن استخدامه في تطبيقات أخرى

### 📦 الملفات

```
gold-price-calculator/
├── gold-calculator.html      # صفحة الحاسبة
├── gold_api_server.py        # سيرفر Flask للـ Web Scraping
├── get_gold_prices.php       # نسخة PHP (اختيارية)
├── requirements.txt          # المكتبات المطلوبة
├── .gitignore               # ملف Git
└── README.md                # التعليمات
```

### 🚀 التشغيل السريع

#### 1. استنساخ المشروع

```bash
git clone https://github.com/your-username/gold-price-calculator.git
cd gold-price-calculator
```

#### 2. تنصيب المتطلبات

```bash
pip install -r requirements.txt
```

#### 3. تشغيل السيرفر

```bash
python3 gold_api_server.py
```

السيرفر سيعمل على: `http://localhost:5000`

#### 4. فتح الصفحة

افتح ملف `gold-calculator.html` في المتصفح.

### 🌐 API Documentation

#### Endpoints

- **GET** `/api/gold-prices` - جلب أسعار الذهب
- **GET** `/health` - فحص حالة السيرفر
- **GET** `/` - صفحة معلومات API

#### Response Example

```json
{
  "success": true,
  "prices": {
    "24": 554.36,
    "22": 508.17,
    "21": 485.07,
    "18": 415.77,
    "14": 323.38
  },
  "updateTime": "01:31:02am",
  "date": "2026/01/13",
  "source": "saudigoldprice.com",
  "timestamp": 1736740800
}
```

### ☁️ الاستضافة

يمكنك استضافة السيرفر على:

#### PythonAnywhere (مجاني) ⭐

1. سجل في [PythonAnywhere](https://www.pythonanywhere.com)
2. ارفع الملفات
3. أنشئ Web App جديد
4. اختر Flask
5. شغل السيرفر

#### Heroku

```bash
# إنشاء Procfile
echo "web: python gold_api_server.py" > Procfile

# Deploy
git init
git add .
git commit -m "Initial commit"
heroku create gold-price-api
git push heroku master
```

#### Railway.app

1. ارفع المشروع على GitHub
2. اربطه مع [Railway](https://railway.app)
3. Railway سيكتشف Python ويشغل السيرفر تلقائياً

### 🔧 الإعدادات

لتغيير رابط API في `gold-calculator.html`:

```javascript
// ابحث عن هذا السطر
const apiUrl = 'http://localhost:5000/api/gold-prices';

// غيره لرابط سيرفرك
const apiUrl = 'https://your-server.com/api/gold-prices';
```

### 📱 الاستخدام بدون سيرفر

إذا لم ترغب بتشغيل سيرفر، الصفحة ستعمل بأسعار افتراضية. فقط حدّث الأسعار يدوياً في الكود.

### 🛠️ التقنيات المستخدمة

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python Flask
- **Web Scraping**: Requests, Regex
- **Styling**: Gradient Design, RTL Support

### 🐛 حل المشاكل

**المتصفح لا يجلب الأسعار؟**
- تأكد من تشغيل السيرفر
- تحقق من رابط API
- افتح Console للأخطاء

**السيرفر يعطي خطأ؟**
- تأكد من تنصيب المكتبات: `pip install -r requirements.txt`
- تحقق من الاتصال بالإنترنت
- راجع terminal logs

### 📄 الترخيص

MIT License - استخدمه بحرية!

### 🤝 المساهمة

المساهمات مرحب بها! افتح Issue أو Pull Request.

### 📞 التواصل

لأي استفسار أو مساعدة، لا تتردد في التواصل!

---

## 🌟 English Version

### 📋 Overview

Gold Price Calculator is a comprehensive tool that allows you to:
- 📊 Fetch live gold prices from saudigoldprice.com
- 🔄 Auto-update every 5 minutes
- 💎 Calculate value of jewelry, bars, and coins
- 💰 Automatically calculate making charges
- 📈 Calculate 15% tax
- 🎨 Professional Arabic interface

### ✨ Features

- ✅ **Real Web Scraping**: Fetches prices directly from saudigoldprice.com
- ✅ **Auto Update**: Prices refresh every 5 minutes
- ✅ **Smart Calculation**: Automatic making charges and tax calculation
- ✅ **Full Support**: Jewelry (24K-14K), Bars (1g-1kg), Coins
- ✅ **Professional Design**: Beautiful responsive Arabic interface
- ✅ **Open API**: Can be used in other applications

### 🚀 Quick Start

#### 1. Clone Repository

```bash
git clone https://github.com/your-username/gold-price-calculator.git
cd gold-price-calculator
```

#### 2. Install Requirements

```bash
pip install -r requirements.txt
```

#### 3. Run Server

```bash
python3 gold_api_server.py
```

Server will run on: `http://localhost:5000`

#### 4. Open Page

Open `gold-calculator.html` in your browser.

### 🌐 API Documentation

See Arabic section above for API details.

### ☁️ Deployment

See deployment options in Arabic section above (PythonAnywhere, Heroku, Railway).

### 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python Flask
- **Web Scraping**: Requests, Regex
- **Styling**: Gradient Design, RTL Support

### 📄 License

MIT License - Free to use!

### 🤝 Contributing

Contributions welcome! Open an Issue or Pull Request.

---

<div align="center">

**Made with ❤️ for the Gold Trading Community**

⭐ Star this repo if you find it useful!

</div>

