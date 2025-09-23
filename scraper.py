import requests
import time

from bs4 import BeautifulSoup
from bs4.element import Tag

from typing import List, Dict, Any

class ListaMercadoLivreScraper:

    def __init__(self, search: str, negative_keywords: list[str] | None = None, pages: int = 3):
        """
        Initialize the Scrapper with a search term and optional negative keywords.

        :param search: The search term to look for on Mercado Livre.
        :param negative_keywords: A list of keywords to filter out unwanted results.
        """
        self.search = search.replace(" ", "-").lower()
        self.url = f"https://lista.mercadolivre.com.br/{self.search}_NoIndex_True"
        self.negative_keywords = negative_keywords if negative_keywords else []
        self.items: List[Dict[str, Any]] = []
        self.session = requests.Session()

    def fetch(self) -> str:
        """
        Fetch the HTML content of the search results page.

        :return: The HTML content as a string.
        """
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        
        # Configurar headers na sessão
        self.session.headers.update(headers)
        
        # Pequeno delay para parecer mais humano
        time.sleep(1)
        
        response = self.session.get(self.url)
        response.raise_for_status()
        return response.text
    
    def parse(self, html: str):
        """
        Parse the HTML content to extract product information.

        :param html: The HTML content as a string.
        :return: A list of dictionaries containing product details.
        """
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_='poly-card')

        for item in items:
            if isinstance(item, Tag):
                title_tag = item.find('h3', class_='poly-component__title-wrapper')
                price_tag = item.find('span', class_='andes-money-amount__fraction')

                if isinstance(title_tag, Tag) and isinstance(price_tag, Tag):
                    title = title_tag.get_text(strip=True).lower()
                    price = price_tag.get_text(strip=True)

                    if not any(neg_kw.lower() in title for neg_kw in self.negative_keywords):
                        self.items.append({
                            'title': title,
                            'price': price
                        })
    
    def get_items(self) -> List[Dict[str, Any]]:
        """
        Get the list of filtered items.

        :return: A list of dictionaries containing product details.
        """
        return self.items