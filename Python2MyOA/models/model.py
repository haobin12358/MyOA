# *- coding:utf8 *-
# 兼容linux系统
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))  # 增加系统路径
# 引用python类
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine, Integer, String, Text

# 引用项目类配置文件
from config import dbconfig as cfg

import pymysql

# 获取和mysql的连接引擎格式 "数据库://用户名:密码@ip(:端口号)/databse名(?charset=字符集)" ()里是可选内容
DB_PARAMS = "{0}://{1}:{2}@{3}/{4}?charset={5}".format(
    cfg.sqlenginename, cfg.username, cfg.password, cfg.host, cfg.database, cfg.charset)
mysql_engine = create_engine(DB_PARAMS, echo=True)

# 实例化基础表，这个这个基础类可以关联到数据库的具体字段
Base = declarative_base()


# 用户表
class User(Base):
    __tablename__ = "Users"
    Uid = Column(String(64), primary_key=True)
    Uname = Column(String(32), nullable=False)
    Upwd = Column(String(32), nullable=False)
    Utype = Column(Integer, nullable=False)
    Unum = Column(String(64), nullable=False)
    Udep = Column(String(128), nullable=False)
    Utel = Column(String(16), nullable=False)
    UCid = Column(String(64), nullable=False)
    Usalary = Column(Integer)


class Approvals(Base):
    __tablename__ = "Approvals"
    Aid = Column(String(64), primary_key=True)
    Uid = Column(String(64), nullable=False)
    Astatus = Column(Integer, nullable=False)
    Aindex = Column(Integer, nullable=False)
    Tid = Column(String(64), nullable=False)


class Examiners(Base):
    __tablename__ = "Examiners"
    Eid = Column(String(64), primary_key=True)
    Aindex = Column(Integer, nullable=False)
    Enum = Column(Integer, nullable=False)
    Uid = Column(String(64), nullable=False)


class Opinions(Base):
    __tablename__ = "Opininons"
    Oid = Column(String(64), primary_key=True)
    Aid = Column(String(64), nullable=False)
    Uid = Column(String(64), nullable=False)
    Oinfo = Column(Text, nullable=False)


class Template(Base):
    __tablename__ = "Template"
    Tid = Column(String(64), primary_key=True)
    Tinfo = Column(Text, nullable=False)
    Tinfotype = Column(Integer, nullable=False)


class File(Base):
    Fid = Column(String(64), primary_key=True)
    Fname = Column(String(255), nullable=False)
    Faddr = Column(Text)
    Frole = Column(Integer)
    Fsaw = Column(Text)
    Uid = Column(String(64))

class databse_deal():
    def __init__(self):
        self.conn = pymysql.connect(host=cfg.host, user=cfg.username, passwd=cfg.password, charset=cfg.charset)
        self.cursor = self.conn.cursor()

    def create_database(self):
        sql = "create database if not exists {0} DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;".format(
            cfg.database)
        print sql
        try:
            self.cursor.execute(sql)
        except Exception, e:
            print(e)
        finally:
            self.conn_close()

    def drop_database(self):
        sql = "drop database if exists {0} ;".format(
            cfg.database)
        print sql
        try:
            self.cursor.execute(sql)
        except Exception, e:
            print(e)

        finally:
            self.conn_close()

    def conn_close(self):
        self.conn.close()


def create():
    databse_deal().create_database()
    Base.metadata.create_all(mysql_engine)


def drop():
    databse_deal().drop_database()


if __name__ == "__main__":
    '''
    运行该文件就可以在对应的数据库里生成本文件声明的所有table
    如果需要清除数据库，输入drop
    如果需要创建数据库 输入任意不包含drop的字符
    '''
    action = raw_input("indropadsput action")
    if "drop" in action:
        drop()
    else:
        create()
