import json
from pprint import pprint
from flask import jsonify


with open('data.json') as data_file:
    db = json.load(data_file)

def ping():
    return "ping success"

def print_db(key):
    pprint (db[key])
    return jsonify(db[key])

def add_taxi(taxi):
    db["taxis"].append(taxi)
    return success
