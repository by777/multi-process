# -*- coding: utf-8 -*-
# @TIME : 2022/4/14 10:30
# @AUTHOR : Xu Bai
# @FILE : 06.thread_process_cpu_bound.py
# @DESCRIPTION :
import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

PRIMES = [112272535095293] * 100


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    sqrt_n = int(math.floor(math.sqrt(number)))
    for i in range(3, sqrt_n + 1, 2):
        if number % i == 0:
            return False
    return True


def single_thread():
    for number in PRIMES:
        is_prime(number)


def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


if __name__ == '__main__':
    start1 = time.time()
    single_thread()
    end1 = time.time()

    star2 = time.time()
    multi_thread()
    end2 = time.time()

    start3 = time.time()
    multi_process()
    end3 = time.time()

    print(f'single thread cost: {end1 - start1}'
          f'multi thread cost: {end2 - star2}'
          f'multi process cost: {end3 - start3}')
