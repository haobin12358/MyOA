# *- coding:utf8 *-
# 兼容linux系统
import sys
import os
sys.path.append(os.path.dirname(os.getcwd())) # 增加系统路径
import uuid


class MakeData():
    def __init__(self):
        self.user = SUsers()

    def make_id(self):
        user_ids = []
        i = 0
        while i < 22:
            user_ids.append(uuid.uuid4())
            i = i + 1
        return user_ids
    def add_users(self, user_ids):
        i = 0
        name = "test"
        pwd = "123"
        utype = 100
        while i < 22:
            self.user.add_user(user_ids[i], name + str(i), pwd, utype)
            i = i + 1
            if i > 10:
                utype = 101

if __name__ == "__main__":
    data = MakeData()
    tuser_ids, tstudent_ids, tteacher_ids, tcompetition_ids, tteam_ids = data.make_id()
    data.add_users(tuser_ids)
    data.add_students(tuser_ids, tstudent_ids)
    data.add_teachers(tuser_ids, tteacher_ids)
    data.add_competitions(tcompetition_ids)
    data.add_team(tteam_ids, tcompetition_ids)
    data.add_tsstudent(tteam_ids, tstudent_ids)
    data.add_tsteacher(tteam_ids, tteacher_ids)
    data.add_stech(tstudent_ids)
    data.add_scuse(tstudent_ids)
    data.add_tcuse(tteacher_ids)