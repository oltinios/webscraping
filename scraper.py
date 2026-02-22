import httpx
from selectolax.parser import HTMLParser

def get_html(base_url, page):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
    resp = httpx.get(base_url + str(page), headers=headers)
    html = HTMLParser(resp.text)
    return html

def parse_page(html):
    products = html.css('li[class="max-md:border-b-size-sm max-md:border-color-default"]') # need to wrap it up because most parsers cant handle colons in the class names

    product_list = []

    for product in products:
        item = {
            "name": extract_text(product, ".mb-xs.font-bold"),
            "price": extract_text(product, "span[data-testid=product-price]"),
            "offers": extract_text(product, "span[data-testid=roundel]")
        }
        product_list.append(item)
    return product_list

def extract_text(html, sel):
    try:
        return html.css_first(sel).text()
    except AttributeError:
        return None

def main():
    base_url = "https://www.diy.com/painting-decorating/paint.cat?Location=Interior&page="
    for i in range(1,10):
        print(i)
        html = get_html(base_url, i)
        data = parse_page(html)
        print(data)

if __name__ == "__main__":
    main()

# https://www.diy.com/painting-decorating/paint.cat?Location=Interior&page=2