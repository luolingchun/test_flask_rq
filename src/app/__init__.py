# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 13:37
# @Author  : llc
# @File    : __init__.py


from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_rq2 import RQ
from config import config

db = SQLAlchemy()
rq2 = RQ()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    CORS(app)
    db.init_app(app)
    rq2.init_app(app)

    from .apis import api
    api.init_app(app)
    # 注册蓝本
    # from .apis import api_blueprint as api_blueprint1
    # app.register_blueprint(blueprint=api_blueprint1)

    return app
