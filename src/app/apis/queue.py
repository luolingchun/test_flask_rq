# -*- coding: utf-8 -*-
# @Time    : 2019/6/27 10:08
# @Author  : llc
# @File    : queue.py

from flask_restplus import Resource, Namespace
from config import Config
from app.defines import StatesCode

__version__ = 'v1'
ns = Namespace(f'{__version__}/queues', description='队列管理 API接口')


@ns.route('')
class QueueAPI(Resource):
    @ns.doc(id='get queue list', description='获取队列列表')
    def get(self):
        """获取队列列表"""
        return {"code": StatesCode.SUCCESS, "data": Config.RQ_QUEUES}
