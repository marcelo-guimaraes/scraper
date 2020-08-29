from bs4 import BeautifulSoup
import requests

URL = 'https://www.amazon.com.br/dp/B07TZLF17T?pf_rd_r=MFJ91KJQFRGMTVGJ35CV&pf_rd_p=2382743f-480e-414a-9ea1-df2d1bbc531a'

headers = {"User-Agent":'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="price_inside_buybox").get_text()

print(title.strip())