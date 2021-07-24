from datetime import datetime, date
from bson import ObjectId
import isodate as iso
from flask.json import JSONEncoder


class MongoJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime, date)):
            return iso.datetime_isoformat(o)
        if isinstance(o, ObjectId):
            return str(o)
        else:
            return super().default(o)
