# *- coding:utf8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))  # 增加系统路径

# 引用python类

from flask_restful import Resource
from controller.CUsers import CUser

class AUsers(Resource):
    def __init__(self):
        self.cuser = CUser()

    def post(self, users):
        # 所有user的post接口 通过eval实例化的controller来执行

        apis = {
            "login": "self.cuser.login()",
            "pwdchange": "self.cuser.pwdchange()",
        }
        if users not in apis:
            from config.message import NO_APIS as message
            from config.status import OUT as status
            from config.statuscode import NO_APIS as statuscode

            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }

        return eval(apis.get(users))

    def get(self,users):
        # get 接口
        return self.cuser.userinfo()

