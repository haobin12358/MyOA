# *- coding:utf8 *-
# *- coding:utf8 *-
# 兼容linux系统
import sys
import os
sys.path.append(os.path.dirname(os.getcwd())) # 增加系统路径
#引用python类
from flask import request
import json
#引用项目类
from service.SUsers import SUsers

class CUser():
    def __init__(self):
        self.susers = SUsers()

    def login(self):
        """
        该方法用来登录 需要判断密码是否正确
        :return:
        """
        form = request.data #获取前端发送的body体
        print str(form)
        # 判断body体不为空
        if str(form) == "" or str(form) == "[]":
            from config.message import PARAM_MISS as message
            from config.status import INNER as status
            from config.statuscode import PARAM_MISS as statuscode

            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }
        form = json.loads(form)
        num_list =self.susers.get_all_unum() #获取数据库中存在的uname

        # 判断Unum是否存在
        if str(form["Unum"]) not in num_list:
            from config.message import NO_USER as message
            from config.status import INNER as status
            from config.statuscode import NO_USER as statuscode

            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }

        Upwd = self.susers.get_upwd_by_unum(form["Unum"])  # 根据用户名获取数据库的密码
        print(Upwd)
        print(form["Upwd"])
        # 判断session是否异常
        if Upwd == False:
            from config.message import SYSTEM_ERROR as message
            from config.status import OUT as status
            from config.statuscode import SYSTEM_ERROR as statuscode

            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }

        # 判断用户名与密码匹配
        if Upwd != str(form["Upwd"]):
            from config.message import PWD_ERROR_LOGIN as message
            from config.status import INNER as status
            from config.statuscode import PWD_ERROR_LOGIN as statuscode

            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }

        Uid = self.susers.get_uid_by_unum(form["Unum"])  # 根据用户名获取数据库的id
        from config.message import LOGIN_OK as message
        from config.statuscode import LOGIN_OK as statuscode
        message["Uid"] = Uid
        return {
            "messages": message,
            "statuscode": statuscode,
        }

    def changepwd(self):
        """
        该方法用于修改密码
        :return:
        """
        form = request.data  # 获取前端发送的body体
        print str(form)
        # 判断body体不为空
        if str(form) == "" or str(form) == "[]":
            from config.message import PARAM_MISS as message
            from config.status import INNER as status
            from config.statuscode import PARAM_MISS as statuscode

            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }


    def userinfo(self):
        """
        该方法查看用户的所有信息
        :return:
        """
        pass
