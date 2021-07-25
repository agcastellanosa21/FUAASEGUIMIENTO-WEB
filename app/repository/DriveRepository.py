from app.config import ConnectionDB


class DriveRepository:
    connection = None

    def __init__(self, app):
        self.connection = ConnectionDB.ConnectionDB(app).connect()

    def findByCart(self, plaque):
        drive = self.connection.db.drive.find_one({"vehicle": plaque})
        return drive
