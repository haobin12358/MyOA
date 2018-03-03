# *- coding:utf8 *-
# 兼容linux系统
import sys
import os
sys.path.append(os.path.dirname(os.getcwd())) # 增加系统路径
#引用项目类
import DBSession
from models import model
from common.TransformToList import trans_params


# 操作user表的相关方法
class SUsers():
    def __init__(self):
        try:
            self.session = DBSession.db_session() #实例化
            self.status = True #session异常的判断标记
        except Exception as e:
            print e.message
            self.status = False

    # 插入单个user
    def add_user(self, uid, uname, upwd, utype):
        """
        :param uid: 主键
        :param uname: 用户名
        :param upwd: 密码
        :param utype: 用户类型100-102
        :return: 插入数据正常返回 True,数据库操作异常返回 False
        """
        try:
            # 实例化一个User对象 并赋值
            new_user = model.Uers()
            new_user.Uid = uid
            new_user.Uname = uname
            new_user.Upwd = upwd
            new_user.Utype = utype
            # 数据库操作添加一个User数据
            self.session.add(new_user)
            self.session.commit()
            self.session.close()
            return True
        except Exception as e:
            # 数据库操作异常的话执行rollback 来回退操作
            self.session.rollback()
            self.session.close()
            print e.message
            return False
