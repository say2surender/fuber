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

@APP.route('/admin/taxi/', methods=['POST'])
def add_taxi():
    return service.print_db("taxis")


if __name__ == "__main__":
    APP.run(
        "127.0.0.1",
        7777,
        debug=True,
        threaded=True
    )
