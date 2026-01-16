#!/usr/bin/env python3
"""
Flask API Server لجلب أسعار الذهب من saudigoldprice.com
استخدام:
1. نصب المتطلبات: pip install flask requests beautifulsoup4
2. تشغيل السيرفر: python3 gold_api_server.py
3. الوصول للـ API: http://localhost:5000/api/gold-prices
"""

from flask import Flask, jsonify
from flask_cors import CORS
import requests
import re
from datetime import datetime
import logging

app = Flask(__name__)
CORS(app)  # للسماح بالوصول من أي domain

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scrape_gold_prices():
    """جلب أسعار الذهب من saudigoldprice.com"""
    url = 'https://saudigoldprice.com/'
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        html = response.text
        
        prices = {}
        
        # استخراج الأسعار باستخدام regex
        patterns = {
            '24': r'سعر جرام الذهب عيار 24[\s\S]*?<td[^>]*>([\d\.]+)</td>',
            '22': r'سعر جرام الذهب عيار 22[\s\S]*?<td[^>]*>([\d\.]+)</td>',
            '21': r'سعر جرام الذهب عيار 21[\s\S]*?<td[^>]*>([\d\.]+)</td>',
            '18': r'سعر جرام الذهب عيار 18[\s\S]*?<td[^>]*>([\d\.]+)</td>',
            '14': r'سعر جرام الذهب عيار 14[\s\S]*?<td[^>]*>([\d\.]+)</td>'
        }
        
        for karat, pattern in patterns.items():
            match = re.search(pattern, html)
            if match:
                prices[karat] = float(match.group(1))
        
        # استخراج وقت التحديث
        update_time = ''
        match = re.search(r'(\d{2}:\d{2}:\d{2}[ap]m)', html, re.IGNORECASE)
        if match:
            update_time = match.group(1)
        
        # استخراج التاريخ
        date = ''
        match = re.search(r'(\d{4}/\d{2}/\d{2})', html)
        if match:
            date = match.group(1)
        
        if prices:
            logger.info(f"تم جلب الأسعار بنجاح: {prices}")
            return {
                'success': True,
                'prices': prices,
                'updateTime': update_time,
                'date': date,
                'source': 'saudigoldprice.com',
                'timestamp': int(datetime.now().timestamp())
            }
        else:
            raise Exception('فشل في استخراج الأسعار من HTML')
    
    except Exception as e:
        logger.error(f"خطأ في جلب الأسعار: {str(e)}")
        # أسعار احتياطية
        return {
            'success': False,
            'error': str(e),
            'fallback': {
                '24': 554.36,
                '22': 508.17,
                '21': 485.07,
                '18': 415.77,
                '14': 323.38
            },
            'timestamp': int(datetime.now().timestamp())
        }

@app.route('/api/gold-prices', methods=['GET'])
def get_gold_prices():
    """API endpoint لجلب أسعار الذهب"""
    result = scrape_gold_prices()
    return jsonify(result)

@app.route('/health', methods=['GET'])
def health_check():
    """للتحقق من عمل السيرفر"""
    return jsonify({'status': 'ok', 'timestamp': int(datetime.now().timestamp())})

@app.route('/', methods=['GET'])
def index():
    """صفحة رئيسية"""
    return '''
    <html dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>Gold Prices API</title>
        <style>
            body { font-family: Arial; padding: 50px; background: #f5f5f5; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; }
            h1 { color: #d4af37; }
            code { background: #f0f0f0; padding: 5px 10px; border-radius: 5px; }
            .endpoint { margin: 20px 0; padding: 15px; background: #f9f9f9; border-left: 4px solid #d4af37; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🏆 Gold Prices API</h1>
            <p>API لجلب أسعار الذهب الحية من saudigoldprice.com</p>
            
            <div class="endpoint">
                <h3>📍 Endpoints:</h3>
                <p><strong>GET</strong> <code>/api/gold-prices</code> - جلب أسعار الذهب</p>
                <p><strong>GET</strong> <code>/health</code> - التحقق من عمل السيرفر</p>
            </div>
            
            <div class="endpoint">
                <h3>📝 مثال على الاستخدام:</h3>
                <code>
                    fetch('/api/gold-prices')<br>
                    &nbsp;&nbsp;.then(res => res.json())<br>
                    &nbsp;&nbsp;.then(data => console.log(data))
                </code>
            </div>
            
            <div class="endpoint">
                <h3>📦 Response Format:</h3>
                <pre>{
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
  "timestamp": 1736740800
}</pre>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    print("🚀 Starting Gold Prices API Server...")
    print("📍 API Endpoint: http://localhost:5000/api/gold-prices")
    print("🏥 Health Check: http://localhost:5000/health")
    app.run(debug=True, host='0.0.0.0', port=5000)
