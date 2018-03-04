# *- coding:utf8 *-
# 兼容linux系统
import sys
import os
sys.path.append(os.path.dirname(os.getcwd())) # 增加系统路径
from service.SUsers import SUsers
import model

change_index = 10  # 循环中改变type的点
info_count = 22  # 需要插入的数据库条数


class MakeData():
    def __init__(self):
        self.user = SUsers()

    def make_id(self):
        import uuid
        user_ids = []
        i = 0
        while i < info_count:
            user_ids.append(str(uuid.uuid4()))
            i = i + 1
        return user_ids

    def add_users(self, uid_list, cid_list):
        for i in range(info_count):
            user_model = model.User()
            user_model.Uid = uid_list[i]
            user_model.Uname = "test{0}".format(i)
            user_model.Upwd = "123"
            user_model.Utype = 100 if i < change_index else 101
            user_model.Unum = "hlf%04d" % i
            user_model.Udep = "CI" if i < change_index else "IT"
            user_model.Utel = "135880461%02d" % i
            user_model.UCid = cid_list[i]
            self.user.add_user(user_model)


if __name__ == "__main__":
    print("start")
    data = MakeData()
    tuser_ids = data.make_id()
    cids = data.make_id()
    data.add_users(tuser_ids, cids)
    print("over")

