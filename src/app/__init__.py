# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 13:37
# @Author  : llc
# @File    : __init__.py


from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_rq2 import RQ
import config

db = SQLAlchemy()
rq2 = RQ()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    CORS(app)
    db.init_app(app)
    rq2.init_app(app)

    from .apis import api
    api.init_app(app)

    return app
