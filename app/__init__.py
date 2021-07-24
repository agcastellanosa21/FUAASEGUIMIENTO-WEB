from flask import Flask, render_template, redirect, jsonify
from datetime import datetime
from flask_pymongo import PyMongo

app = Flask(__name__)
connection = PyMongo(app, "mongodb+srv://agcastellanosa:Mongo123@cluster0.x0gpu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


def startApp(config):
    # Use configuration defined on the config.py
    app.config.from_object(config)
    return app


###############################################################
# DEFINE WEB SERVICES END POINTS
###############################################################

# Route for import sample data
@app.route("/sample-data", methods=["GET"])
def sampleData():
    # Create cart sample data
    connection.db.cart.insert_many([
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
    connection.db.localization.insert_many([
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

    return redirect("/")


# Route used to get the current location list of the carts
@app.route("/localizations", methods=["GET"])
def findAllLocalizations():
    localizations = connection.db.localization.aggregate([{
        "$group": {
            "_id": "$vehicle",
            "vehicle": {"$last": "$vehicle"},
            "date": {"$last": "$date"},
            "longitude": {"$last": "$longitude"},
            "latitude": {"$last": "$latitude"},
            "gps_trace": {"$last": "$gps_trace"},
        }
    }])

    return jsonify([localization for localization in localizations])


###############################################################
# DEFINE RENDERS TEMPLATES END POINTS
###############################################################


# Route to render cart list
@app.route("/carts", methods=["GET"])
def findAllCarts():
    carts = connection.db.cart.find()
    return render_template("pages/carts.html", carts=carts)


# Main route to render location dashboard
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


