# *- coding:utf8 *-
# 兼容linux系统
import sys
import os
sys.path.append(os.path.dirname(os.getcwd())) # 增加系统路径
# 引用python类
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine, Integer, String, Text

# 引用项目类配置文件
from config import dbconfig as cfg

# 获取和mysql的连接引擎格式 "数据库://用户名:密码@ip(:端口号)/databse名(?charset=字符集)" ()里是可选内容
DB_PARAMS = "{0}://{1}:{2}@{3}/{4}?charset={5}".format(
    cfg.sqlenginename, cfg.username, cfg.password, cfg.host, cfg.database, cfg.charset)
mysql_engine = create_engine(DB_PARAMS, echo=True)

# 实例化基础表，这个这个基础类可以关联到数据库的具体字段
Base = declarative_base()


# 用户表
class Uers(Base):
    __tablename__ = "Users"
    Uid = Column(String(64), primary_key=True)
    Uname = Column(String(32), nullable=False)
    Upwd = Column(String(32), nullable=False)
    Utype = Column(Integer, nullable=False)
    Unum = Column(String(64), nullable=False)
    Udep = Column(String(128), nullable=False)
    Utel = Column(String(16), nullable=False)
    UCid = Column(String(64), nullable=False)
