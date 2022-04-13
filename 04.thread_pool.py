# -*- coding: utf-8 -*-
# @TIME : 2022/4/13 20:15
# @AUTHOR : Xu Bai
# @FILE : 04.thread_pool.py
# @DESCRIPTION :
from concurrent.futures import ThreadPoolExecutor, as_completed
from blog_spider import urls, craw, parser

# craw
with ThreadPoolExecutor() as pool:
    htmls = pool.map(craw, urls)
    htmls = list(zip(urls, htmls))
    for url, html in htmls:
        print(url, len(html))
# parser
with ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(parser, html)
        futures[future] = url
    # for future, url in futures.items():
    #     print(url, future.result())
    for future in as_completed(futures):
        url = futures[future]
        print(url, future.result())
