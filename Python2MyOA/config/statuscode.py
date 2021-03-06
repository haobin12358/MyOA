# *- coding:utf8 *-
"""
-------------404--------
"""
NO_APIS = 404001
SYSTEM_ERROR = 404100  # 系统错误
"""
-------------405---------
"""
PARAM_MISS = 405201  # 参数缺失
NO_USER = 405101  # 用户不存在
PWD_ERROR_LOGIN = 405102  # 登录时密码错误
PWD_ERROR_OLD = 405103  # 修改密码时原始密码错误
PWD_EQUAL_OLD = 405104  # 原始密码与新密码相同
PWD_OUTER = 405105  # 密码过长
UID_MISS = 405106  # uid参数为空
NO_UID = 405107  # 不存在此uid
LOGIN_OK = 200  # 登录成功
DB_CONN_ERROR = "405108"  # 数据库连接失败
