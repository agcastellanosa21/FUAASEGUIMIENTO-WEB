from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


def startApp(config):
    # Use configuration defined on the config.py
    app.config.from_object(config)
    return app
