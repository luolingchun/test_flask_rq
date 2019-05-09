# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 15:18
# @Author  : llc
# @File    : job_api.py
from flask_restplus import Resource, Namespace, reqparse
from app.utils.queues import default_queue, low_queue
from app.jobs.job_calc import add

__version__ = 'v1'
ns = Namespace(f'{__version__}/job', description='任务管理 API接口')

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument(name='job_id', type=str, location='args', required=True, help='任务id')


@ns.route('')
class JobListAPI(Resource):
    @ns.doc(id='get job list', description='获取任务列表')
    def get(self):
        """获取任务列表"""
        jobs = default_queue.get_jobs()
        job_list = []
        for job in jobs:
            job_list.append(job.get_id())
        return {'code': 0, 'data': job_list}

    @ns.doc(id='post job', description='添加任务')
    def post(self):
        '''添加任务'''
        job = default_queue.enqueue(add, args=(1, 2))
        job_id = job.get_id()
        return {'code': 0, 'data': job_id}


@ns.route('/<job_id>')
class JobAPI(Resource):
    @ns.doc(id='get job', description='获取任务')
    @ns.expect(parser)
    def get(self, job_id):
        '''获取任务'''
        job = default_queue.fetch_job(job_id)
        if not job:
            return {'code': 0, 'data': 'not found job id'}
        return {'code': 0, 'data': job.get_status()}

    @ns.doc(id='delete job', description='删除任务')
    @ns.expect(parser)
    def delete(self, job_id):
        '''删除任务'''
        job = default_queue.fetch_job(job_id)
        if not job:
            return {'code': 0, 'data': 'not found job id'}
        job.delete()
        return {'code': 0, 'data': job_id}
