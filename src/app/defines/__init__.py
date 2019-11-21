# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 17:15
# @Author  : llc
# @File    : __init__.py


class StatesCode:
    UNKNOWN_ERROR = -2  # 未知错误
    SUCCESS = 0  # 成功
    QUEUE_NOT_EXIST = 101  # 队列不存在
    JOB_NOT_EXIST = 102  # 任务不存在
    JOB_STATUS_NO_EXIST = 103  # 任务状态不存在
    JOB_OPERATION_ERROR=104
