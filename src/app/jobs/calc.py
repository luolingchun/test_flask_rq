# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 15:17
# @Author  : llc
# @File    : jobs.py


import time
from rq.job import Job
from app import rq2


def add(x, y, job_id=None):
    # print(job_id)
    job = Job.fetch(job_id, connection=rq2.connection)
    print(job.meta)
    for i in range(10):
        time.sleep(1)
        job.meta['progress'] = i * 10
        job.save_meta()
    print(job.meta)
    return x + y
