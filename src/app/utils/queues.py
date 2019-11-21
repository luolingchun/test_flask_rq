# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 16:42
# @Author  : llc
# @File    : queues.py

from app import rq2

default_queue = rq2.get_queue()  # 默认队列

high_queue = rq2.get_queue('high')  # 优先队列

low_queue = rq2.get_queue('low')  # 低级队列

pause_queue = rq2.get_queue('pause')  # 暂停队列

queue_dict = {
    "default": default_queue,  # 默认队列
    "high": high_queue,  # 优先队列
    "low": low_queue,
    "pause": pause_queue,  # 暂停队列
}
