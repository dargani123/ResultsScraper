import re
from bs4 import BeautifulSoup

with open('test.html') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
print(soup.find(text=re.compile("Revenue")))
