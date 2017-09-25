from flask import Flask, jsonify, request
import service
APP = Flask(__name__)

service.calculate_available_taxis()

@APP.route('/')
def ping():
    """ A health check for app

    """
    return service.ping()

@APP.route('/user/taxi/request/', methods=['POST'])
def request_taxi():
    """ Returns a available taxi, if it is within 50km range
    ---
        parameters:
          - in: body
            name: body
            description: No Parameters required
        responses:
            success:
                description: Response sent
                schema:
                    type: "dict"
            error:
                description: Error sent
                schema:
                    type: "str"
                value:
                    "No taxis around you"
    """
    error = None
    code = 200
    if hasattr(request, 'json') and request.json is not None:
        ride, error = service.request_taxi(request.json["loc"], request.json["type"])
        if error is not None:
            code = 404
            ride = error
    return jsonify(ride), code

@APP.route('/user/taxi/end/', methods=['POST'])
def end_ride():
    """ Ends a ride, returns fare and distance_covered, and other ride details
    ---
        parameters:
          - in: body
            name: body
            description: No Parameters required
        responses:
            success:
                description: Response sent
                schema:
                    type: "dict"
            error:
                description: Error sent
                schema:
                    type: "str"
                value:
                    "No ride to end"
    """
    error = None
    code = 200
    if hasattr(request, 'json') and request.json is not None:
        ride, error = service.end_ride(request.json)
        if error is not None:
            ride = error
            code = 400
    return jsonify(ride), code

if __name__ == "__main__":
    APP.run(
        "127.0.0.1",
        7777,
        debug=True,
        threaded=True
    )
