# *- coding:utf8 *-
# 兼容linux系统
import sys
import os
sys.path.append(os.path.dirname(os.getcwd())) # 增加系统路径
#引用项目类
from models import model
import DBSession
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


    #获取全部的工号
    @trans_params
    def get_all_unum(self):
        num_list = None
        try:
            num_list = self.session.query(model.User.Unum).all()
        except Exception as e:
            print e.message
        finally:
            self.session.close()
        return num_list

    #根据工号获取密码
    def get_upwd_by_unum(self, unum):
        upwd = None
        try:
            upwd = self.session.query(model.User.Upwd).filter_by(Unum = unum).scalar()
        except Exception as e:
            print e.message
            return False
        finally:
            self.session.close()
        return upwd

    #根据工号获取uid
    def get_uid_by_unum(self, unum):
        uid = None
        try:
            uid = self.session.query(model.User.Uid).filter_by(Unum = unum).scalar()
        except Exception as e:
            print e.message
        finally:
            self.session.close()
        return uid

    # 插入一个user 初始化数据时用到
    def add_user(self, user):
        try:
            self.session.add(user)
            self.session.commit()
        except Exception, e:
            print(e)
        finally:
            self.session.close()