import json
from pprint import pprint
from flask import jsonify
import utils
import datetime
from dateutil import parser

with open('data.json') as data_file:
    db = json.load(data_file)

available_taxis = []
live_rides = []

def calculate_available_taxis():
    for taxi in db["taxis"]:
        if taxi["is_available"] == True:
            available_taxis.append(
                                {"taxi_id":taxi["id"],
                                "category": taxi["taxi"]["category"],
                                "curr_loc": taxi["curr_loc"]
                                })
    return available_taxis

def request_taxi(loc, type):
    global live_rides
    global available_taxis

    nearest_taxi = None
    nearest_distance = 50
    print(loc, type)
    for taxi in available_taxis:
        if taxi["category"] == type:
            this_taxi_distance = utils.eu_distance(loc, taxi["curr_loc"])
            if this_taxi_distance < nearest_distance:
                nearest_distance = this_taxi_distance
                nearest_taxi = taxi
    if nearest_taxi is not None:
        available_taxis.remove(nearest_taxi)
        ride = {
        "id": 1,
        "taxi": nearest_taxi,
        "start_time": datetime.datetime.utcnow(),
        "end_time": 0,
        "start_loc": loc,
        "end_loc": {
                    "lat": 0,
                    "long": 0
                    }
        }
        live_rides.append(ride)
        return ride
    else:
        return "No rides near you, Sorry."

def end_ride(ride):
    live_ride_found = False
    global live_rides
    global available_taxis
    available_taxis.append(
                        {"taxi_id": ride["taxi"]["taxi_id"],
                        "category": ride["taxi"]["category"],
                        "curr_loc": ride["end_loc"]
                        })
    live_rides = [x for x in live_rides if x['id'] not in [ride]]
    for i in range(len(live_rides)):
        if live_rides[i]['id'] == ride["id"]:
            del live_rides[i]
            live_ride_found = True
            break
    print(live_rides)
    if live_ride_found:
        ride["time_elapsed"] = (parser.parse(ride["start_time"]) - parser.parse(ride["start_time"])).total_seconds()
        ride["distance_covered"] = utils.eu_distance(ride["start_loc"], ride["end_loc"])
        ride["fare"] = ride["time_elapsed"] + ride["distance_covered"] * 2
        with open("rides.log", "a") as log:
            log.write(str(ride["id"])+" - "+str(ride["fare"])+" dodgecoins")
        return ride
    else:
        return "Not a valid ride"

def ping():
    return "ping success"

def print_db(key):
    pprint (db[key])
    return jsonify(db[key])

def add_taxi(taxi):
    db["taxis"].append(taxi)
    return success
