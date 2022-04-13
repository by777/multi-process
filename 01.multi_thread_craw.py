# -*- coding: utf-8 -*-
# @TIME : 2022/4/13 15:08
# @AUTHOR : Xu Bai
# @FILE : 01.multi_thread_craw.py
# @DESCRIPTION :
import threading
import time

import blog_spider

from timeit import timeit


def single_thread():
    print('single_thread begin \n')
    for url in blog_spider.urls:
        blog_spider.craw(url)
    print('single_thread end \n')


def multi_thread():
    print('multi_thread begin \n')
    threads = []
    for url in blog_spider.urls:
        threads.append(
            threading.Thread(target=blog_spider.craw, args=(url,))
        )
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()  # 等待结束
    print('multi_thread end \n')


if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()

    start1 = time.time()
    multi_thread()
    end1 = time.time()

    print(f'single thread cost {end - start} seconds, multi thread cost {end1 - start1} seconds')
