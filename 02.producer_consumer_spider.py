# -*- coding: utf-8 -*-
# @TIME : 2022/4/13 15:31
# @AUTHOR : Xu Bai
# @FILE : 02.producer_consumer_spider.py
# @DESCRIPTION :
from queue import Queue
import random
import time
import threading

import blog_spider


# 生产者
def do_craw(url_queue: Queue, html_queue: Queue):
    while True:
        url = url_queue.get()
        html = blog_spider.craw(url)

        html_queue.put(html)
        print(threading.current_thread().name, f"craw {url}, url size: {url_queue.qsize()}")
        time.sleep(random.randint(1, 2))


# 消费者
def do_parser(html_queue: Queue, fout):
    while True:
        html = html_queue.get()
        results = blog_spider.parser(html)
        for result in results:
            fout.write(str(result) + '\n')

        print(threading.current_thread().name, f"results size {len(results)}, html_queue size: {html_queue.qsize()}")
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    '''
    一个复杂的爬虫可以分很多的模块，模块之间通过Queue来通信的，
    通过Queue，主线程把数据扔进去，
    把Q传递给生产者，生产者产出中间的数据，
    消费者线程对数据处理，得到最终的产出。
    '''
    url_queue = Queue()
    html_queue = Queue()
    # 生产
    for url in blog_spider.urls:
        url_queue.put(url)
    for idx in range(3):
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue), name=f'craw_{idx}')
        t.start()
    # 消费
    fout = open('02.data.txt', 'w')
    for idx in range(2):
        t = threading.Thread(target=do_parser, args=(html_queue, fout), name=f'parser_{idx}')
        t.start()
