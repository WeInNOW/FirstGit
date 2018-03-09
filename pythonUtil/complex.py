import json
from datetime import *
import time


from bson.objectid import ObjectId
'''
对于json.dump(case,XXXX...)
case中有一些类型不能默认处理，如 ObjectId、datetime等，需要自定义一个类，传入到dump()方法中，
cls=CJsonEncoder)
'''
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj,ObjectId):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)