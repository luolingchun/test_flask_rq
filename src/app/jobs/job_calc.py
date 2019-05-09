# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 15:17
# @Author  : llc
# @File    : jobs.py
from app.webapp import rq


@rq.job
def add(x, y):
    return x + y
