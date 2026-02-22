import httpx
from selectolax.parser import HTMLParser

def get_html():
    url = "https://www.diy.com/painting-decorating/paint.cat?Location=Interior"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}

    resp = httpx.get(url, headers=headers)
    html = HTMLParser(resp.text)
    return html

def parse_page(html):
    products = html.css('li[class="max-md:border-b-size-sm max-md:border-color-default"]') # need to wrap it up because most parsers cant handle colons in the class names

    for product in products:
        item = {
            "name": extract_text(product, ".mb-xs.font-bold"),
            "price": extract_text(product, "span[data-testid=product-price]"),
            "offers": extract_text(product, "span[data-testid=roundel]")
        }
        print(item)

def extract_text(html, sel):
    try:
        return html.css_first(sel).text()
    except AttributeError:
        return None

def main():
    html = get_html()
    parse_page(html)

if __name__ == "__main__":
    main()