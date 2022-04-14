# -*- coding: utf-8 -*-
# @TIME : 2022/4/14 10:41
# @AUTHOR : Xu Bai
# @FILE : 07.flask_process_pool.py
# @DESCRIPTION :
import json

import flask
from concurrent.futures import ProcessPoolExecutor

import math

# 多进程与多线程的区别，多进程他们之间的环境是完全隔离的
# 当定义pool的时候，它所依赖的函数必须已经声明完了
# 所以，pool必须放在最下面
# process_pool = ProcessPoolExecutor()
app = flask.Flask(__name__)


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


@app.route('/is_prime/<numbers>')
def api_is_prime(numbers):
    numbers_list = [int(x) for x in numbers.split(',')]
    results = process_pool.map(is_prime, numbers_list)
    return json.dumps(
        dict(zip(
            numbers_list, results
        ))
    )


if __name__ == '__main__':
    # 不仅放到最下面，还必须在main里
    process_pool = ProcessPoolExecutor()
    app.run()
