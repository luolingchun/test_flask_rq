# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 15:17
# @Author  : llc
# @File    : jobs.py


import time


def add(x, y):
    # time.sleep(100)
    for i in range(10):
        print(i)
        time.sleep(4)
    return x + y
