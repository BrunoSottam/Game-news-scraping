from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import re

links = ["https://ign.com","https://gamespot.com"]

def gameSiteScraper(links):
    for each in links:
      page = urlopen(each)
      html = page.read().decode("utf-8")
      soup = BeautifulSoup(html,"html.parser")
      soup_title = soup.find("title")
      soup_title = str(soup_title)
      title_pattern = '<title>(.*?)</title>'
      title = re.findall(title_pattern, soup_title)
      soup_news = soup.find_all("h3")
      news_title = soup_news
      print(title)
      time.sleep(3)
      print(news_title)
    

