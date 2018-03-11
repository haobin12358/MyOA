# *- coding:utf8 *-
# 兼容linux系统
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))  # 增加系统路径
# 引用项目类
from models import model
import DBSession
from common.TransformToList import trans_params


# 操作user表的相关方法
class SUsers():
    def __init__(self):
        """
        self.session 数据库连接会话
        self.status 判断数据库是否连接无异常
        """
        self.session, self.status = DBSession.get_session()

    # 获取全部的工号
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

    # 根据工号获取密码
    def get_upwd_by_unum(self, unum):
        upwd = None
        try:
            upwd = self.session.query(model.User.Upwd).filter_by(Unum=unum).scalar()
        except Exception as e:
            print e.message
            return False
        finally:
            self.session.close()
        return upwd

    # 根据工号获取uid
    def get_uid_by_unum(self, unum):
        uid = None
        try:
            uid = self.session.query(model.User.Uid).filter_by(Unum=unum).scalar()
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

    # 获取全部uid
    @trans_params
    def get_all_uid(self):
        uid_list = None
        try:
            uid_list = self.session.query(model.User.Uid).all()
        except Exception as e:
            print e.message
            return False
        finally:
            self.session.close()
        return uid_list

    # 根据uid获取密码
    def get_upwd_by_uid(self, uid):
        upwd = None
        try:
            upwd = self.session.query(model.User.Upwd).filter_by(Uid=uid).scalar()
        except Exception as e:
            print e.message
            return False
        finally:
            self.session.close()
        return upwd

    # 根据uid更新密码
    def update_upwd_by_uid(self, uid, form):
        try:
            self.session.query(model.User).filter_by(Uid=uid).update(form)
            self.session.commit()
            return True
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()

    # 用户uid获取用户个人信息
    def get_user_info_by_uid(self, uid):
        user_abo = None
        try:
            user_abo = self.session.query(model.User.Uname, model.User.Utype, model.User.Ucid,
                                      model.User.Unum, model.User.Udep, model.User.Utel).filter_by(Uid=uid).first()
        except Exception as e:
            print e.message
        finally:
            self.session.close()
        return user_abo
