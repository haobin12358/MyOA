# *- coding:utf8 *-
from controller.CSubs import CSubs
from flask_restful import Resource


class ASubs(Resource):
    def __init__(self):
        self.csubs = CSubs()

    def post(self, sub):
        apis = {
            "new": "self.csubs.new()",
            "undo": "self.csubs.undo()",
            "deal": "self.csubs.deal()",
            "initiated": "self.csubs.initiated()",
            "update": "self.csubs.update()",
            "delete": "self.csubs.delete()"
        }
        if sub not in apis:
            from config.message import NO_APIS as message
            from config.status import OUT as status
            from config.statuscode import NO_APIS as statuscode

            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }

        return eval(apis[sub])


