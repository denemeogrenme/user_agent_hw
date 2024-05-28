# user_agent_hw

## Description
"Books to Scrape" web sitesinden kitap bilgilerini toplamak için Python kullanarak web scraping yapmayı amaçlamaktayım. Requests kütüphanesi kullanılarak HTTP istekleri gönderilmekte ve BeautifulSoup ile HTML içeriği ayrıştırılmakta. Projeye "hw_web_scrarping" projesinden farklı olarak isteğin bir tarayıcıdan geliyormuş gibi görünmesini sağlamak için User-Agent başlığı eklenmiştir.

## Features
- "http://books.toscrape.com/" sitesinden kitap başlıkları, fiyatları ve stok bilgilerini toplar.
- Verileri CSV dosyası formatında kaydeder.

## Dependencies
- `requests` library
- `beautifulsoup4` library
- `pandas` library
