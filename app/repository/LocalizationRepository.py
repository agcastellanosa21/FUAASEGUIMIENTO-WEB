from app.config import ConnectionDB


class LocalizationRepository:
    connection = None

    def __init__(self, app):
        self.connection = ConnectionDB.ConnectionDB(app).connect()

    def findAllCartsLocalization(self):
        localizations = self.connection.db.localization.aggregate([{
            "$group": {
                "_id": "$vehicle",
                "vehicle": {"$last": "$vehicle"},
                "date": {"$last": "$date"},
                "longitude": {"$last": "$longitude"},
                "latitude": {"$last": "$latitude"},
                "gps_trace": {"$last": "$gps_trace"},
            }
        }])
        return localizations
