# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 16:46
# @Author  : llc
# @File    : worker.py

from app.webapp import rq, application

# 开始任务
with application.app_context():
    default_worker = rq.get_worker()
    default_worker.work()
