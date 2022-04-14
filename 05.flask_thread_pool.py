# -*- coding: utf-8 -*-
# @TIME : 2022/4/13 20:30
# @AUTHOR : Xu Bai
# @FILE : 05.flask_thread_pool.py
# @DESCRIPTION : 使用进程池加速flask
import threading
import time

import flask
import json

from concurrent.futures import ThreadPoolExecutor

app = flask.Flask(__name__)
pool = ThreadPoolExecutor()


def read_file():
    time.sleep(0.1)
    return 'file result'


def read_db():
    time.sleep(0.2)
    return 'db result'


def read_api():
    time.sleep(0.3)
    return 'api result'


@app.route('/')
def index():
    """
    result_file = read_file()
    result_db = read_db()
    result_api = read_api()
    """
    result_file = pool.submit(read_file)
    result_db = pool.submit(read_db)
    result_api = pool.submit(read_api)
    # 这个时候返回的不是3个字符串了，二十3个future对象

    return json.dumps({
        'result_file': result_file.result(),
        'result_db': result_db.result(),
        'result_api': result_api.result()
    })


if __name__ == '__main__':
    app.run()
