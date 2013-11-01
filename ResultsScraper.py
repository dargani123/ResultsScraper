from bs4 import BeautifulSoup

html = open('test.html').read()
print(html)

soup = BeautifulSoup(html, 'html.parser')

print(soup.find("Revenue"))