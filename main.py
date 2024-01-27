
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time


class WebScraper:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {'User-Agent': UserAgent().random}

    def fetch_html(self, url):
        try:
            response = self.session.get(url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching HTML: {e}")
            return None

    def scrape_headlines(self, url):
        html_content = self.fetch_html(url)
        if html_content:
            soup = BeautifulSoup(html_content, 'html.parser')

            # Print the entire HTML content for inspection
            print(soup.prettify())

            # Update class based on the actual HTML structure
            headlines = soup.find_all('h2', class_='highlight')  # Update class based on actual HTML structure

            for index, headline in enumerate(headlines, 1):
                print(f"{index}. {headline.text.strip()}")


if __name__ == "__main__":
    scraper = WebScraper()
    news_url = 'https://timesofindia.indiatimes.com/news'  # Replace with actual URL

    print("\nNews Headlines:")
    scraper.scrape_headlines(news_url)

