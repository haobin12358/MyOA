# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd())) # 增加系统路径
#引用python类
from flask import request
import json
#引用项目类
from service.SSubs import SSubs
from common.get_str import get_str


class CSubs():
    def __init__(self):
        self.ssubs = SSubs()

    def check_connection(self):
        if self.ssubs.status is False:
            from config.message import DB_CONN_ERROR
            raise Exception(DB_CONN_ERROR)

    def new(self):
        """
        该方法处理添加审批
        :return:
        """

        pass

    def undo(self):
        """
        该方法处理
        :return:
        """
        pass

    def deal(self):
        pass

    def initiated(self):
        pass

    def update(self):
        pass
