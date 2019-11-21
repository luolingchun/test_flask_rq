# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 13:39
# @Author  : llc
# @File    : __init__.py

from flask_restplus import Api

api = Api(
    version='v1.0',
    title='任务管理API',
    description='基于flask和rq的任务管理系统',
    doc='/swagger',
)

from .job import ns as job_ns

api.add_namespace(job_ns)
