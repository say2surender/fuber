import json
from pprint import pprint
from flask import jsonify
import utils

with open('data.json') as data_file:
    db = json.load(data_file)

available_cars = []



def calculate_available_cars():
    for car in db["taxis"]:
        if car["is_available"] == True:
            available_cars.append(
                                {"car_id":car["id"],
                                "type": car["car"]["category"],
                                "h_loc": utils.h_loc(car["curr_loc"])
                                })
    return available_cars


def ping():
    return "ping success"

def print_db(key):
    pprint (db[key])
    return jsonify(db[key])

def add_taxi(taxi):
    db["taxis"].append(taxi)
    return success
