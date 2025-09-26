from scraper import ListaMercadoLivreScraper

def main():

    scraper = ListaMercadoLivreScraper(search="notebook lenovo ideapad i3", negative_keywords=["recondicionado", "game"])
    html = scraper.fetch()
    scraper.parse(html)
    items = scraper.get_items()

    for item in items:
        print(f"Title: {item['title']}, Price: {item['price']}")

if __name__ == "__main__":
    main()