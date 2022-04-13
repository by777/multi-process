# -*- coding: utf-8 -*-
# @TIME : 2022/4/13 19:55
# @AUTHOR : Xu Bai
# @FILE : lock_current.py
# @DESCRIPTION :
import threading
import time

lock = threading.Lock()


class Account:
    def __init__(self, balance):
        self.balance = balance


def draw(account: Account, amount):
    with lock:
        if account.balance >= amount:
            time.sleep(0.1)  # 确保一致出问题
            print(threading.current_thread().name, '取钱成功')
            account.balance -= amount
            print(threading.current_thread().name, '余额', account.balance)
        else:
            print(threading.current_thread().name, '余额不足，取钱失败')


if __name__ == '__main__':
    account = Account(1000)
    ta = threading.Thread(name='ta', target=draw, args=(account, 800))
    tb = threading.Thread(name='tb', target=draw, args=(account, 800))
    ta.start()
    tb.start()
