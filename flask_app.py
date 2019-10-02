# flask_app.py
from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "Goodbye ≈Earth until next time!"


@app.route("/api")
def api():
    data = pd.DataFrame({'words':['one','two'], 'numbers':[1,2]})
    return data.to_json(orient='records')
