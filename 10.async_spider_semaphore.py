# -*- coding: utf-8 -*-
# @TIME : 2022/4/14 11:08
# @AUTHOR : Xu Bai
# @FILE : 08.async_spider.py
# @DESCRIPTION :
import asyncio
import time

import aiohttp

import blog_spider

semaphore = asyncio.Semaphore(10)


async def async_craw(url):
    async with semaphore:
        print('craw url', url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                result = await resp.text()
                # 控制并发度，最多10个
                await asyncio.sleep(5)
                print(f'craw url:{url}, {len(result)}')


loop = asyncio.get_event_loop()
tasks = [loop.create_task(async_craw(url)) for url in blog_spider.urls]
start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
# 一般来说单线程异步速度会快于多线程并发
print(f'use time: {end - start}')
