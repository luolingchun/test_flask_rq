# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 15:08
# @Author  : llc
# @File    : webapp.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_rq2 import RQ
from config import config

db = SQLAlchemy()
rq = RQ()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    rq.init_app(app)

    from .apis import api
    api.init_app(app)
    # 注册蓝本
    # from .apis import api_blueprint as api_blueprint1
    # app.register_blueprint(blueprint=api_blueprint1)

    return app


application = create_app('production')

if __name__ == '__main__':
    application.run(host='0.0.0.0', port='4444', debug=True)
