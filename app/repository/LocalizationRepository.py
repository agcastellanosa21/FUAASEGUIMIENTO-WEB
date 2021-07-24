from app.config import ConnectionDB


class LocalizationRepository:
    connection = None

    def __init__(self, app):
        self.connection = ConnectionDB.ConnectionDB(app).connect()

    # The last location of each of the vehicles is obtained,
    # to be displayed on the main monitoring panel
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

    # Obtain the current location of the vehicle,
    # the license plate number is passed as a parameter
    def findCurrentLocalizationByCart(self, plaque):
        localization = self.connection.db.localization.find_one({"vehicle": plaque}, sort=[("date", -1)])
        return localization

    # Obtain the vehicle's location history,
    # the license plate number is passed as a parameter
    def findLocalizationHistoryByCart(self, plaque):
        localization = self.connection.db.localization.find({"vehicle": plaque}).sort("date", -1)
        return localization
