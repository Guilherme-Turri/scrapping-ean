from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

class EANWebScraper:
    def __init__(self, initial_url, ean_list):
        self.initial_url = initial_url
        self.ean_list = ean_list
        self.arr_of_urls = []
        self.driver = webdriver.Chrome()

    def initialize_driver(self):
        self.driver.get(self.initial_url)
        self.driver.maximize_window()

    def search_and_collect_urls(self):
       for ean in self.ean_list:
            search_element = self.driver.find_element("xpath", '//*[@id="__next"]/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/form/div/input')
            search_element.send_keys(Keys.CONTROL + "a")
            search_element.send_keys(Keys.DELETE)
            search_element.send_keys(ean)
            search_element.send_keys(Keys.ENTER)
            time.sleep(5)

            html_content = self.driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')

            try:
                element = soup.find('a', class_='hyperlinkstyles__Link-j02w35-0 hbKsSa')
                self.arr_of_urls.append('www.paodeacucar.com' + element['href'])
            except:
                self.arr_of_urls.append('NotFound')
    def close_driver(self):
        self.driver.quit()
