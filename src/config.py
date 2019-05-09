# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 13:36
# @Author  : llc
# @File    : config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):  # 所有配置类的父类，通用的配置写在这里
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BUNDLE_ERRORS = True
    UPLOAD_TMP_FILE = os.path.join(basedir, 'tmp')

    # 配置redis
    REDIS_HOST, REDIS_PORT = os.environ.get('REDIS_PORT', 'tcp://202.107.245.46:3333')[6:].split(':')
    RQ_REDIS_DB = 0
    RQ_REDIS_URL = 'redis://{}:{}/{}'.format(REDIS_HOST, REDIS_PORT, RQ_REDIS_DB)
    # 配置RQ
    RQ_QUEUES = ['default', 'low']


class DevelopmentConfig(Config):  # 开发环境配置类
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data-dev.db')


class TestingConfig(Config):  # 测试环境配置类
    TESTING = True
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data-test.db')


class ProductionConfig(Config):  # 生产环境配置类
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data.db')


config = {  # config字典注册了不同的配置，默认配置为开发环境，本例使用开发环境
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

CONFIG_LAVEL = 'default'
