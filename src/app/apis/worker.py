# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 16:38
# @Author  : llc
# @File    : worker.py

from flask_restplus import Resource, Namespace
from app import rq2
from rq.worker import Worker
from app.defines import StatesCode

__version__ = 'v1'
ns = Namespace(f'{__version__}/workers', description='worker管理 API接口')


@ns.route('')
class WorkerAPI(Resource):
    @ns.doc(id='get job list', description='获取worker列表')
    def get(self):
        """获取worker列表"""
        worker_list = []
        total = Worker.count(connection=rq2.connection)
        workers = Worker.all(connection=rq2.connection)

        for worker in workers:
            worker_list.append({
                "queue_names": worker.queue_names(),
                "current_job": worker.get_current_job(),
                "heartbeat": worker.heartbeat(),
                "name": worker.name,
                "state": worker.get_state(),
            })
        return {"code": StatesCode.SUCCESS, "total": total, "data": worker_list}
