# user_agent_hw

## Description
Bu proje, "Books to Scrape" web sitesinden kitap bilgilerini toplamak için Python kullanarak web scraping yapmayı amaçlamanmakta. Requests kütüphanesini kullanarak HTTP istekleri gönderir ve BeautifulSoup ile HTML içeriğini ayrıştırır. Projeye "hw_web_scrarping" projesinden farklı olarak isteğin bir tarayıcıdan geliyormuş gibi görünmesini sağlamak için User-Agent başlığı eklenmiştir.

## Features
- "http://books.toscrape.com/" sitesinden kitap başlıkları, fiyatları ve stok bilgilerini toplar.
- Verileri CSV dosyası formatında kaydeder.

## Dependencies
- `requests`
- `beautifulsoup4`
- `pandas`
