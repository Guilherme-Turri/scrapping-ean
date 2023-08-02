from ean_scraper import EANWebScraper
from config import arr_of_ean, initial_url

if __name__ == "__main__":
    scraper = EANWebScraper(initial_url, arr_of_ean)
    scraper.initialize_driver()
    scraper.search_and_collect_urls()
    print(scraper.arr_of_urls)
    scraper.close_driver()