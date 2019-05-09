# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 13:37
# @Author  : llc
# @File    : __init__.py


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    from .apis import api
    api.init_app(app)
    # 注册蓝本
    # from .apis import api_blueprint as api_blueprint1
    # app.register_blueprint(blueprint=api_blueprint1)

    return app
