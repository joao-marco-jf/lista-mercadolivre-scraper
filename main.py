from scraper import ListaMercadoLivreScraper

def main():

    scraper = ListaMercadoLivreScraper(search="iphone 16 pro", negative_keywords=["max"])
    html = scraper.fetch()
    scraper.parse(html)
    items = scraper.get_items()

    for item in items:
        print(f"Title: {item['title']}, Price: {item['price']}")

if __name__ == "__main__":
    main()