# *- coding:utf8 *-
NO_APIS = "the apis is not found"
PARAM_MISS = "missing some parameters !"  # 参数缺失
PWD_ERROR_LOGIN = "the user or password error. "  # 登录时用户或密码错误
WD_ERROR_OLD = "the old password error. "  # 修改密码时原始密码错误
PWD_EQUAL_OLD = "the new password is same as old password. "  # 原始密码与新密码相同
PWD_OUTER = "the password is too long. "  # 密码过长
NO_USER = "the user is not found ."  # 用户不存在
SYSTEM_ERROR = "System is abnormal !" # 系统错误
LOGIN_OK = {
    "Uid":"",
    "message":"login is ok !"
}
# 405102  # 密码错误 api 文档中描述error，和405103类似故不重复