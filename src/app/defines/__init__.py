# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 17:15
# @Author  : llc
# @File    : __init__.py

class StatesCode:
    UNKNOWN_ERROR = -2  # 未知错误
    SUCCESS = 0  # 成功
    QUEUE_NOT_EXIST = 101  # 队列不存在
    JOB_NOT_EXIST = 102  # 任务不存在
    JOB_STATUS_NO_EXIST = 103  # 任务状态不存在


QUEUE_HELP = 'high：优先队列\ndefault：默认队列\nlow：低级队列'
QUEUE_ALL_HELP = 'all：全部\nhigh：优先队列\ndefault：默认队列\nlow：低级队列'

JOB_STATUS_HELP = 'queued：排队\nstarted：开始\nfinished：完成\nfailed：失败'
