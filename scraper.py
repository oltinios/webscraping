import httpx
from selectolax.parser import HTMLParser

url = "https://www.diy.com/painting-decorating/paint.cat?Location=Interior"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}

resp = httpx.get(url, headers=headers)
print(resp)
