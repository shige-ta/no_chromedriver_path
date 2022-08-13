# coding: UTF-8
from bs4 import BeautifulSoup
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
 
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://--------------")
time.sleep(5)
html = driver.page_source.encode('utf-8')

soup = BeautifulSoup(html, "html.parser")
for i in soup.find_all('img'):
    print(i.get('src'))