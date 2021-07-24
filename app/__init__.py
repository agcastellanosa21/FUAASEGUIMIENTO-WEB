from flask import Flask, render_template, redirect, jsonify
from app.repository import SampleDataRepository
from app.repository import CartRepository
from app.repository import LocalizationRepository

app = Flask(__name__)


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
    SampleDataRepository.SampleDataRepository(app).load()
    return redirect("/")


# Route used to get the current location list of the carts
@app.route("/localizations", methods=["GET"])
def findAllLocalizations():
    localizations = LocalizationRepository.LocalizationRepository(app).findAllCartsLocalization()
    return jsonify([localization for localization in localizations])


###############################################################
# DEFINE RENDERS TEMPLATES END POINTS
###############################################################


# Route to render cart list
@app.route("/carts", methods=["GET"])
def findAllCarts():
    carts = CartRepository.CartRepository(app).findAll()
    return render_template("pages/carts.html", carts=carts)


# Main route to render location dashboard
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


