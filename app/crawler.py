import requests
from bs4 import BeautifulSoup


def crawl_ncc():
    url = "https://www.ncc.gov.tw/chinese/news.aspx"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_items = []
    for item in soup.select('.newsTitle a'):
        title = item.text.strip()
        link = "https://www.ncc.gov.tw" + item['href']
        news_items.append({'title': title, 'link': link})

    return news_items


def crawl_bbc():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_items = []
    for item in soup.select('.gs-c-promo-heading'):
        title = item.text.strip()
        link = item['href']
        if not link.startswith('http'):
            link = "https://www.bbc.com" + link
        news_items.append({'title': title, 'link': link})

    return news_items


def crawl_reuters():
    url = "https://www.reuters.com/news/archive"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_items = []
    for item in soup.select('.story-content a'):
        title = item.text.strip()
        link = "https://www.reuters.com" + item['href']
        news_items.append({'title': title, 'link': link})

    return news_items


def crawl_all_sources():
    ncc_news = crawl_ncc()
    bbc_news = crawl_bbc()
    reuters_news = crawl_reuters()

    all_news = ncc_news + bbc_news + reuters_news
    return all_news
