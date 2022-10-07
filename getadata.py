import requests
import json
from bs4 import BeautifulSoup

[print('\n') for i in range(10)]


def find_urls(query):
    wikiapiurl = f'https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search={query}'

    urls = json.loads(requests.get(url=wikiapiurl).text)[3]
    urls = urls
    return urls


def get_text(url):
    html = requests.get(url=url).text
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = soup.find_all('p')
    texts = ''.join([paragraph.text for paragraph in paragraphs])
    return texts




subjects = ['mathematics', 'science', 'history', 'computer_science', 'music']


for subject in subjects:
    urls = find_urls(subject)
    all_wiki_pages = ''.join([get_text(url) for url in urls])

    filename = f'{subject}.txt'
    with open(f'school-subject-predictor/articles/{filename}','w') as f:
        f.write(all_wiki_pages)

