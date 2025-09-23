from scraper import ListaMercadoLivreScraper

def main():

    scrapper = ListaMercadoLivreScraper(search="iphone 16 pro", negative_keywords=["max"])
    html = scrapper.fetch()
    scrapper.parse(html)
    items = scrapper.get_items()

    for item in items:
        print(f"Title: {item['title']}, Price: {item['price']}")

if __name__ == "__main__":
    main()