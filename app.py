from flask import Flask, jsonify, request
import service
APP = Flask(__name__)


@APP.route('/')
def ping():
    return service.ping()

@APP.route('/initiate/')
def initiate():
    return jsonify(service.calculate_available_taxis())

@APP.route('/taxis/all')
def print_taxis():
    return service.print_db("taxis")

@APP.route('/user/taxi/request/', methods=['POST'])
def request_taxi():
    if hasattr(request, 'json') and request.json is not None:
        ride = service.request_taxi(request.json["loc"], request.json["type"])
    return jsonify(ride)

@APP.route('/user/taxi/end/', methods=['POST'])
def end_ride():
    if hasattr(request, 'json') and request.json is not None:
        ride = service.end_ride(request.json)
    return jsonify(ride)

if __name__ == "__main__":
    APP.run(
        "127.0.0.1",
        7777,
        debug=True,
        threaded=True
    )
