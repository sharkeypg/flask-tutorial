# flask_app.py
from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "Goodbye ≈Earth until next time!"


@app.route("/api",methods=["POST"])
def api():
    x = {'a':1,'b':2}
    return jsonify(x)
