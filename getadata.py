import requests
import json
from bs4 import BeautifulSoup

print('\n'*10)


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
    new_query = subject
    all_wiki_pages = ''

    for i in range(2):
        urls = find_urls(new_query)
        all_wiki_pages = all_wiki_pages.join([get_text(url) for url in urls])
        try:
            new_query = urls[1][30:]
        except Exception:
            break



    filename = f'articles/{subject}.txt'
    with open(f'{filename}','w') as f:
        f.write(all_wiki_pages)

