# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 13:36
# @Author  : llc
# @File    : config.py

import os

# 配置redis
REDIS_HOST, REDIS_PORT = os.environ.get('REDIS_PORT', 'tcp://192.168.2.28:3333')[6:].split(':')
RQ_REDIS_DB = 0
RQ_REDIS_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/{RQ_REDIS_DB}'
# 配置RQ
RQ_QUEUES = ('default', 'high', 'low')
RQ_QUEUES_ALL = ('all', 'high', 'default', 'low')
RQ_JOB_STATUS = ('queued', 'started', 'deferred', 'finished', 'failed')

QUEUE_HELP = 'default：默认队列\nhigh：优先队列\nlow：低级队列'
QUEUE_ALL_HELP = 'all：全部\nhigh：优先队列\ndefault：默认队列\nlow：低级队列'
JOB_STATUS_HELP = 'queued：排队\nstarted：开始\ndeferred:推迟\nfinished：完成\nfailed：失败'

TIMEOUT = 3600 * 24  # 1天
