import json
from pprint import pprint
from flask import jsonify
import utils
import datetime
from dateutil import parser

with open('data.json') as data_file:
    db = json.load(data_file)

# Global Variables, which can be kept in memory
available_taxis = []
live_rides = []

# health check service
def ping():
    return "ping success"

# One time initiation function to load the available_taxis to in memory db
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

    # setting default responses
    ride = error = None
    nearest_taxi = None

    # minimum radius for searching a taxi is 50km
    nearest_distance = 50

    try:
        # getting nearest taxi
        for taxi in available_taxis:
            if taxi["category"] == type:
                this_taxi_distance = utils.eu_distance(loc, taxi["curr_loc"])
                if this_taxi_distance < nearest_distance:
                    nearest_distance = this_taxi_distance
                    nearest_taxi = taxi

        # initiate a live_ride and add to live_rides
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
        else:
            raise LookupError("Sorry, Taxi Not found within 50km range")
    except LookupError as err:
        error = err.args
    return ride, error

def end_ride(ride):
    global available_taxis
    # setting default responses
    error = None
    live_ride_found = False
    # de-allocating a taxi, making it available for further rides
    available_taxis.append(
                        {"taxi_id": ride["taxi"]["taxi_id"],
                        "category": ride["taxi"]["category"],
                        "curr_loc": ride["end_loc"]
                        })

    try:
        # remove ride from live_rides
        for i in range(len(live_rides)):
            if live_rides[i]['id'] == ride["id"]:
                del live_rides[i]
                live_ride_found = True
                break

        # generate meta of ride, for fare calculation and write fare in log
        if live_ride_found:
            ride["time_elapsed"] = (parser.parse(ride["start_time"]) - parser.parse(ride["start_time"])).total_seconds()
            ride["distance_covered"] = utils.eu_distance(ride["start_loc"], ride["end_loc"])
            ride["fare"] = ride["time_elapsed"] + ride["distance_covered"] * 2
            with open("rides.log", "a") as log:
                log.write(str(ride["id"])+" - "+str(ride["fare"])+" dodgecoins")
                log.write("\n")
        else:
            raise LookupError("Sorry, No such ride found")
    except LookupError as err:
        error = err.args
    return ride, error
