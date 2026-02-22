import httpx
from selectolax.parser import HTMLParser

url = "https://www.diy.com/painting-decorating/paint.cat?Location=Interior"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}

resp = httpx.get(url, headers=headers)
html = HTMLParser(resp.text)

# print(html.css_first("title").text())

products = html.css('li[class="max-md:border-b-size-sm max-md:border-color-default"]') # need to wrap it up because most parsers cant handle colons in the class names
i = 0
j = 0

while i < len(products):
    j += 1
    i += 1

def extract_text(html, sel):
    try:
        return html.css_first(sel).text()
    except AttributeError:
        return None
        

for product in products:
    item = {
        "name": extract_text(product, ".mb-xs.font-bold"),
        "price": extract_text(product, "span[data-testid=product-price]"),
        "offers": extract_text(product, "span[data-testid=roundel]")
    }
    # print(product.css_first(".mb-xs.font-bold").text())

    print(item)

print(j, "Products")