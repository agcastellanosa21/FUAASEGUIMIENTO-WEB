from flask import Flask, render_template, redirect, jsonify, request
from datetime import datetime

from app.config.MongoJSONEncoder import MongoJSONEncoder
from app.config.ObjectIdConverter import ObjectIdConverter
from app.repository import SampleDataRepository
from app.repository import CartRepository
from app.repository import LocalizationRepository
from app.repository import DriveRepository

app = Flask(__name__)


def startApp(config):
    # Use configuration defined on the config.py
    app.config.from_object(config)
    app.json_encoder = MongoJSONEncoder
    app.url_map.converters['objectid'] = ObjectIdConverter
    return app


###############################################################
# DEFINE WEB SERVICES END POINTS
###############################################################

# Route for import sample data
@app.route("/sample-data", methods=["GET"])
def sampleData():
    SampleDataRepository.SampleDataRepository(app).load()
    return redirect("/")


# Route used to get the current location list of the carts
@app.route("/localizations", methods=["GET"])
def findAllLocalizations():
    localizations = LocalizationRepository.LocalizationRepository(app).findAllCartsLocalization()
    return jsonify([localization for localization in localizations])


# Route to get car location details
# @param plaque
@app.route("/localization-detail/<plaque>", methods=["GET"])
def cartLocalizationDetail(plaque):
    currentLocalization = LocalizationRepository.LocalizationRepository(app).findCurrentLocalizationByCart(plaque)
    localizationHistory = LocalizationRepository.LocalizationRepository(app).findLocalizationHistoryByCart(plaque)

    return jsonify({
        "currentLocalization": currentLocalization,
        "localizationHistory": [localization for localization in localizationHistory]
    })


# Route for creating locations
@app.route("/create-localization", methods=["POST"])
def createLocalization():
    body = request.get_json()

    if "longitude" not in body:
        return jsonify({
            "status": "Bad Request",
            "message": "The longitude is required",
            "date": datetime.now()
        }), 400

    if "latitude" not in body:
        return jsonify({
            "status": "Bad Request",
            "message": "The latitude is required",
            "date": datetime.now()
        }), 400

    if "gps_trace" not in body:
        return jsonify({
            "status": "Bad Request",
            "message": "The gps_trace is required",
            "date": datetime.now()
        }), 400

    if "vehicle" not in body:
        return jsonify({
            "status": "Bad Request",
            "message": "The vehicle is required",
            "date": datetime.now()
        }), 400

    LocalizationRepository.LocalizationRepository(app).create(body)

    return jsonify({
        "status": "Ok",
        "message": "Location created successfully",
        "date": datetime.now()
    }), 200


###############################################################
# DEFINE RENDERS TEMPLATES END POINTS
###############################################################


# Route to render the cart location detail view
# @param plate
@app.route("/cart-localization/<plaque>", methods=["GET"])
def cartLocalization(plaque):
    drive = DriveRepository.DriveRepository(app).findByCart(plaque)
    return render_template("pages/cart-localization.html", plaque=plaque, drive=drive)


# Route to render cart list
@app.route("/carts", methods=["GET"])
def findAllCarts():
    carts = CartRepository.CartRepository(app).findAll()
    return render_template("pages/carts.html", carts=carts)


# Main route to render location dashboard
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
