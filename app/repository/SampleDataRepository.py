from app.config import ConnectionDB
from datetime import datetime


class SampleDataRepository:
    connection = None

    def __init__(self, app):
        self.connection = ConnectionDB.ConnectionDB(app).connect()

    def load(self):
        # Create cart sample data
        self.connection.db.cart.insert_many([
            {
                "plaque": "WTO304",
                "capacity": "20 TONS",
                "characteristic": "20 ton white van",
                "image_name": "cart_image.png"
            },
            {
                "plaque": "WTM856",
                "capacity": "10 TONS",
                "characteristic": "10 ton white van",
                "image_name": "cart_image.png"
            },
            {
                "plaque": "REM098",
                "capacity": "50 TONS",
                "characteristic": "50 ton white van",
                "image_name": "cart_image.png"
            },
            {
                "plaque": "GHT001",
                "capacity": "60 TONS",
                "characteristic": "60 ton white van",
                "image_name": "cart_image.png"
            }
        ])

        # Create localization sample data
        self.connection.db.localization.insert_many([
            {
                "vehicle": "WTO304",
                "latitude": "6.152448",
                "longitude": "-75.622995",
                "gps_trace": "",
                "date": datetime.now()
            },
            {
                "vehicle": "WTM856",
                "latitude": "4.4283209",
                "longitude": "-75.2052694",
                "gps_trace": "",
                "date": datetime.now()
            },
            {
                "vehicle": "REM098",
                "latitude": "4.678769",
                "longitude": "-74.0579026",
                "gps_trace": "",
                "date": datetime.now()
            },
            {
                "vehicle": "GHT001",
                "latitude": "3.4176511",
                "longitude": "-76.5096121",
                "gps_trace": "",
                "date": datetime.now()
            }
        ])
