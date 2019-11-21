# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 13:36
# @Author  : llc
# @File    : config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """所有配置类的父类，通用的配置写在这里"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BUNDLE_ERRORS = True
    UPLOAD_TMP_FILE = os.path.join(basedir, 'tmp')

    # 配置redis
    REDIS_HOST, REDIS_PORT = os.environ.get('REDIS_PORT', 'tcp://localhost:3333')[6:].split(':')
    RQ_REDIS_DB = 0
    RQ_REDIS_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/{RQ_REDIS_DB}'
    # 配置RQ
    RQ_QUEUES = ['high', 'default', 'low']
    RQ_QUEUES_ALL = ['all', 'high', 'default', 'low']
    RQ_JOB_STATUS = ['queued', 'started', 'finished', 'failed','deferred']
    RQ_DEFAULT_TIMEOUT = 3600 * 24  # 1天


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data-dev.db')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data-test.db')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data.db')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}

CONFIG_LEVEL = 'production'
