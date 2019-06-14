# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 15:08
# @Author  : llc
# @File    : webapp.py

from app import create_app


application = create_app('production')

if __name__ == '__main__':
    application.run(host='0.0.0.0', port='4444', debug=True)
