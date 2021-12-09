import requests
from bs4 import BeautifulSoup

stats = requests.get('https://adventofcode.com/2021/stats')
soup = BeautifulSoup(stats.text, 'html.parser')

most_recent = soup.main.a
print(most_recent.get_text().replace('*', ''))
#print(soup.main.a)
