# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 13:39
# @Author  : llc
# @File    : __init__.py

from flask_restplus import Api

# 实例化 Blueprint 类，两个参数分别为蓝本的名字和蓝本所在包或模块，第二个通常填 __name__ 即可
# api_blueprint = Blueprint('apis', __name__)
api = Api(version='v1.0', title='任务管理服务', description='', doc='/api', prefix='/api')

from .job_api import ns as job_ns

api.add_namespace(job_ns)
