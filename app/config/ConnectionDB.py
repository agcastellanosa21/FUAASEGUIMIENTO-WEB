from flask_pymongo import PyMongo


class ConnectionDB:
    connection = None
    app = None

    def __init__(self, app):
        self.app = app

    def connect(self):
        return PyMongo(self.app, "mongodb+srv://agcastellanosa:Mongo123@cluster0.x0gpu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
