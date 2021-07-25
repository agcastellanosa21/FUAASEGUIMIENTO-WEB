from werkzeug.routing import BaseConverter
from bson import ObjectId


class ObjectIdConverter(BaseConverter):
    def to_python(self, value):
        return ObjectId(value)

    def to_url(self, value):
        return str(value)
