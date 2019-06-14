# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 16:42
# @Author  : llc
# @File    : queues.py

from app import rq

default_queue = rq.get_queue()

low_queue = rq.get_queue('low')
