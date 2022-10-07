import requests
import json
from bs4 import BeautifulSoup

[print('\n') for i in range(10)]


def find_urls(query):
    wikiapiurl = f'https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search={query}'

    urls = json.loads(requests.get(url=wikiapiurl).text)[3]
    urls = urls[:5]
    return urls


def get_text(url):
    html = requests.get(url=url).text
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = soup.find_all('p')
    texts = ''.join([paragraph.text for paragraph in paragraphs])
    return texts



urls = find_urls('biology')
all_wiki_pages = ''.join([get_text(url) for url in urls])

filename = 'biology.txt'
with open(f'school-subject-predictor/{filename}','w') as f:
    f.write(all_wiki_pages)