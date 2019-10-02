# flask_app.py
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "Goodbye ≈Earth until next time!"

test_dict = {'a':1, 'b':2}

@app.route("/api")
def json_ify(data=test_dict):
    return jsonify(data)
