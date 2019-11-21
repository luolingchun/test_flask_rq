# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 15:18
# @Author  : llc
# @File    : job.py

import traceback
from flask import request
from flask_restplus import Resource, Namespace, reqparse
from rq.exceptions import NoSuchJobError, InvalidJobOperation
from rq.job import Job, requeue_job
from rq.registry import StartedJobRegistry, FailedJobRegistry, FinishedJobRegistry, DeferredJobRegistry
from app.defines import StatesCode
from app.jobs.calc import add
from app.utils.queues import queue_dict
from app import rq2
from uuid import uuid4

from config import QUEUE_ALL_HELP, RQ_QUEUES_ALL, RQ_QUEUES, QUEUE_HELP, JOB_STATUS_HELP, RQ_JOB_STATUS, TIMEOUT

ns = Namespace('job', description='任务管理 API接口')

job_list_param_get = reqparse.RequestParser()
job_list_param_get.add_argument(name='queue_name', type=str, choices=RQ_QUEUES_ALL, location='args', required=True,
                                help=QUEUE_ALL_HELP)
job_list_param_get.add_argument(name='job_status', type=str, choices=RQ_JOB_STATUS, location='args', required=True,
                                help=JOB_STATUS_HELP)
job_list_param_post = reqparse.RequestParser()
job_list_param_post.add_argument(name='queue_name', type=str, choices=RQ_QUEUES, location='form', required=True,
                                 help=QUEUE_HELP)


@ns.route('')
class JobListAPI(Resource):
    @ns.doc(id='get job list', description='根据任务状态、队列名称获取任务列表')
    @ns.expect(job_list_param_get)
    def get(self):
        """获取任务列表"""
        args = request.args
        job_status = args.get('job_status')
        queue_name = args.get('queue_name')
        if job_status not in RQ_JOB_STATUS:
            return {'code': StatesCode.JOB_STATUS_NO_EXIST, 'message': '任务状态不存在！'}
        if queue_name not in RQ_QUEUES_ALL:
            return {'code': StatesCode.QUEUE_NOT_EXIST, 'message': '任务队列不存在！'}
        job_list = []
        if job_status == 'queued':
            if queue_name == 'all':
                for queue_name in RQ_QUEUES:
                    job_list += queue_dict[queue_name].get_job_ids()
            else:
                job_list = queue_dict[queue_name].get_job_ids()
        elif job_status == 'started':
            if queue_name == 'all':
                for queue_name in RQ_QUEUES:
                    started_job_registry = StartedJobRegistry(queue=queue_dict[queue_name])
                    job_list += started_job_registry.get_job_ids()
            else:
                started_job_registry = StartedJobRegistry(queue=queue_dict[queue_name])
                job_list = started_job_registry.get_job_ids()
        elif job_status == 'finished':
            if queue_name == 'all':
                for queue_name in RQ_QUEUES:
                    finished_job_registry = FinishedJobRegistry(queue=queue_dict[queue_name])
                    job_list += finished_job_registry.get_job_ids()
            else:
                finished_job_registry = FinishedJobRegistry(queue=queue_dict[queue_name])
                job_list = finished_job_registry.get_job_ids()
        elif job_status == 'failed':
            if queue_name == 'all':
                for queue_name in RQ_QUEUES:
                    failed_job_registry = FailedJobRegistry(queue=queue_dict[queue_name])
                    job_list += failed_job_registry.get_job_ids()
            else:
                failed_job_registry = FailedJobRegistry(queue=queue_dict[queue_name])
                job_list = failed_job_registry.get_job_ids()
        elif job_status == 'deferred':
            if queue_name == 'all':
                for queue_name in RQ_QUEUES:
                    deferred_job_registry = DeferredJobRegistry(queue=queue_dict[queue_name])
                    job_list += deferred_job_registry.get_job_ids()
            else:
                deferred_job_registry = DeferredJobRegistry(queue=queue_dict[queue_name])
                job_list = deferred_job_registry.get_job_ids()
        return {'code': StatesCode.SUCCESS, 'data': job_list}

    @ns.doc(id='post job', description='添加任务')
    @ns.expect(job_list_param_post)
    def post(self):
        """添加任务"""
        form = request.form
        queue_name = form.get('queue_name')
        if queue_name not in RQ_QUEUES:
            return {'code': StatesCode.QUEUE_NOT_EXIST, 'message': '任务队列不存在！'}
        job_id = str(uuid4())
        job = queue_dict[queue_name].enqueue(add, args=(1, 2, job_id), job_id=job_id,
                                             job_timeout=TIMEOUT, )
        # job = queue_dict[queue_name].enqueue(add, args=(1, '2'), job_timeout=RQ_DEFAULT_TIMEOUT)  # 错误任务
        return {'code': 0, 'data': job.get_id()}


job_param = reqparse.RequestParser(bundle_errors=True)
job_param.add_argument(name='job_id', type=str, location='path', required=True, help='任务id')


@ns.route('/<job_id>')
@ns.param('job_id', '任务id', 'path', required=True, type=str)
class JobAPI(Resource):
    @ns.doc(id='get job', description='获取单个任务详情')
    def get(self, job_id):
        """获取单个任务"""
        try:
            job = Job.fetch(job_id, connection=rq2.connection)
        except NoSuchJobError:
            return {'code': StatesCode.JOB_NOT_EXIST, 'message': '任务不存在！'}
        except Exception as e:
            return {'code': StatesCode.UNKNOWN_ERROR, 'message': str(e)}
        info = {
            "id": job.id,
            "origin": job.origin,
            "status": job.get_status(),
            "func_name": job.func_name,
            "args": job.args,
            "kwargs": job.kwargs,
            "result": job.result,
            "timeout": job.timeout,
            "enqueued_at": job.enqueued_at.strftime('%Y-%m-%d %H:%M:%S') if job.enqueued_at else '',
            "started_at": job.started_at.strftime('%Y-%m-%d %H:%M:%S') if job.started_at else '',
            "ended_at": job.ended_at.strftime('%Y-%m-%d %H:%M:%S') if job.ended_at else '',
            "exc_info": job.exc_info,
            "dependent_ids": job.dependent_ids,
            "meta": job.meta
        }
        return {'code': 0, 'data': info}

    @ns.doc(id='requeue job', description='重新开始任务')
    def put(self, job_id):
        """重新开始任务"""
        try:
            requeue_job(job_id, connection=rq2.connection)
        except NoSuchJobError:
            return {'code': StatesCode.JOB_NOT_EXIST, 'message': '任务不存在！'}
        except InvalidJobOperation:
            return {'code': StatesCode.JOB_OPERATION_ERROR, 'message': '只有失败的任务才能重处理！'}
        except Exception as e:
            traceback.print_exc()
            return {'code': StatesCode.UNKNOWN_ERROR, 'message': f'位置错误：{str(e)}'}

        return {'code': 0, 'data': job_id}

    @ns.doc(id='delete job', description='删除任务')
    def delete(self, job_id):
        """删除任务"""
        try:
            job = Job.fetch(job_id, connection=rq2.connection)
        except NoSuchJobError:
            return {'code': StatesCode.JOB_NOT_EXIST, 'message': '任务不存在！'}
        except Exception as e:
            return {'code': StatesCode.UNKNOWN_ERROR, 'message': str(e)}
        job.cancel()
        # job.delete()
        return {'code': 0, 'data': job_id}
