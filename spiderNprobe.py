# https://en.wikipedia.org/wiki/Programmer#

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited_urls = set()


def spider_urls(url, keyword):
    try:
        response = requests.get(url)

    except:
        print(f"Illegal url {url}")

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

    a_tag = soup.find_all('a')
    urls = []

    for tag in a_tag:
        href = tag.get("href")
        if href is not None and href != "":
            urls.append(href)
    #print(urls)

    for u in urls:
        if u not in visited_urls:
            visited_urls.add(u)
            url_join = urljoin(url, u)
            if keyword in url_join:
                print(url_join)
                spider_urls(url_join, keyword)
        else:
            pass

url = input("Paste the URL you would like to use  ")
keyword = input("Enter the keyword to search for in the URL provided  ")
spider_urls(url, keyword)

# https://www.yahoo.com
