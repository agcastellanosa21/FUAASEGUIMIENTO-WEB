from app.config import ConnectionDB


class CartRepository:
    connection = None

    def __init__(self, app):
        self.connection = ConnectionDB.ConnectionDB(app).connect()

    def findAll(self):
        return self.connection.db.cart.find()
