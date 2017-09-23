from flask import Flask
import service
APP = Flask(__name__)


@APP.route('/')
def ping():
    return service.ping()

if __name__ == "__main__":
    APP.run(
        "127.0.0.1",
        7777,
        debug=True,
        threaded=True
    )
