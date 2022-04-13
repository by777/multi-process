# -*- coding: utf-8 -*-
# @TIME : 2022/4/13 15:05
# @AUTHOR : Xu Bai
# @FILE : blog_spider.py
# @DESCRIPTION :
import requests
from bs4 import BeautifulSoup

urls = [
    f'https://www.cnblogs.com/#{page}'
    for page in range(1, 50 + 1)
]


def craw(url):
    r = requests.get(url)
    # print(url, len(r.text))
    return r.text


def parser(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', class_='post-item-title')
    return [(link['href'], link.get_text()) for link in links]


if __name__ == '__main__':
    for result in parser(craw(urls[2])):
        print(result)
