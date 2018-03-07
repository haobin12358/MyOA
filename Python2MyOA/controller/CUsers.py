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
from common.get_str import get_str

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
        print(type(form["Unum"]))
        num_list =self.susers.get_all_unum() # 获取数据库中存在的unum
        print(type(num_list))

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

        print(type(Upwd))
        print(type(form["Upwd"]))
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

    def pwdchange(self):
        """
        该方法用于修改密码
        :return:
        """
        form = request.data  # 获取前端发送的body体，以列表形式呈现
        args = request.args.to_dict() # 获取前端的params参数，以字典形式呈现
        print str(form)
        print(args)
        # 判断Uid参数不为空
        if str(args) == "" or str(args) == "{}":
            from config.message import UID_MISS as message
            from config.status import INNER as status
            from config.statuscode import UID_MISS as statuscode

            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }

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

        uid_list = self.susers.get_all_uid()  # 获取数据库中存在的uid
        print(uid_list)
        # 判断session是否异常
        if uid_list == False:
            from config.message import SYSTEM_ERROR as message
            from config.status import OUT as status
            from config.statuscode import SYSTEM_ERROR as statuscode

            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }

        uid_to_str = get_str(args, "Uid") # 将参数Uid的编码类型转换成str
        # 判断uid存在

        if uid_to_str not in uid_list:
            from config.message import NO_UID as message
            from config.status import INNER as status
            from config.statuscode import NO_UID as statuscode

            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }

        form = json.loads(form)
        upwd = self.susers.get_upwd_by_uid(uid_to_str) # 根据用户名获取数据库的id
        print(upwd)
        # 判断session是否异常
        if upwd == False:
            from config.message import SYSTEM_ERROR as message
            from config.status import OUT as status
            from config.statuscode import SYSTEM_ERROR as statuscode

            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }
        # 判断原始密码输入正确
        print("hello")
        print(type(upwd))
        print(type(form["oldpwd"]))
        print(type(uid_to_str))
        if form["oldpwd"] != upwd:
            from config.message import WD_ERROR_OLD as message
            from config.status import INNER as status
            from config.statuscode import PWD_ERROR_OLD as statuscode

            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }

        # 判断新输入密码与原密码不相同
        if form["oldpwd"] == form["newpwd"]:
            from config.message import PWD_EQUAL_OLD as message
            from config.status import INNER as status
            from config.statuscode import PWD_EQUAL_OLD as statuscode

            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }

        print(uid_to_str)
        # 根据uid修改用户密码
        isupdate = self.susers.update_upwd_by_uid(uid_to_str, {"Upwd": form["newpwd"]})
        # 判断session是否异常
        if isupdate == False:
            from config.message import SYSTEM_ERROR as message
            from config.status import OUT as status
            from config.statuscode import SYSTEM_ERROR as statuscode

            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }
        print(isupdate)
        from config.status import OK as status
        return {
            "message": "pwdchange ok !",
            "status": status,
        }
    def userinfo(self):
        """
        该方法查看用户的所有信息
        :return:
        """
        args = request.args.to_dict()  # 获取前端的params参数,以列表形式呈现
        # 判断Uid参数不为空
        if str(args) == "" or str(args) == "{}":
            from config.message import UID_MISS as message
            from config.status import INNER as status
            from config.statuscode import UID_MISS as statuscode

            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }

        uid_list = self.susers.get_all_uid()  # 获取数据库中存在的uid
        print(uid_list)
        # 判断session是否异常
        if uid_list == False:
            from config.message import SYSTEM_ERROR as message
            from config.status import OUT as status
            from config.statuscode import SYSTEM_ERROR as statuscode

            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }

        uid_to_str = get_str(args, "Uid")  # 将参数Uid的编码类型转换成str
        # 判断uid存在
        print(type(uid_to_str))
        print(type(uid_list[0]))
        if uid_to_str not in uid_list:
            from config.message import NO_UID as message
            from config.status import INNER as status
            from config.statuscode import NO_UID as statuscode

            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }

        # 根据uid获取个人信息
        userabo_of_controller = {}
        userabo_of_service = self.susers.get_user_info_by_uid(uid_to_str)
        userabo_of_controller["Uname"] = userabo_of_service.Uname
        userabo_of_controller["Utype"] = userabo_of_service.Utype
        userabo_of_controller["Ucid"] = userabo_of_service.Ucid
        userabo_of_controller["Unum"] = userabo_of_service.Unum
        userabo_of_controller["Udep"] = userabo_of_service.Udep
        userabo_of_controller["Utel"] = userabo_of_service.Utel
        return {
            "status": 200,
            "message": "get userinfo success !",
            "userinfo": userabo_of_controller,
        }
