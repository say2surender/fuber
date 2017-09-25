from flask import Flask, jsonify
import service
APP = Flask(__name__)


@APP.route('/')
def ping():
    return service.ping()

@APP.route('/initiate/')
def initiate():
    return jsonify(service.calculate_available_cars())

@APP.route('/taxis/all')
def print_taxis():
    return service.print_db("taxis")

@APP.route('/user/taxi/request', methods=['POST'])
def request_taxi():
    if hasattr(request, 'json') and request.json is not None:
        nearest_taxi, error = service.get_taxi(request.json["loc"], request.json["type"])
        if nearest_taxi is not None:
            return "Taxi hailed succesfully " + nearest_taxi["id"]

    return service.print_db("taxis")


if __name__ == "__main__":
    APP.run(
        "127.0.0.1",
        7777,
        debug=True,
        threaded=True
    )
