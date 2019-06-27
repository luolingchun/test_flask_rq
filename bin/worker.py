# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 16:46
# @Author  : llc
# @File    : worker.py

from app import rq2
from app.webapp import application

# 开始任务
with application.app_context():
    default_worker = rq2.get_worker()
    # default_worker.work(burst=True) #全部任务完成后退出
    default_worker.work()
