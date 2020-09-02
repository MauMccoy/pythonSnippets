from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://cucamelon.shop/aboutUs.html"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
