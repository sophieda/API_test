from flask import Flask, request
from threading import Thread

import utils


class API:
    """This class is supposed to contain the web server.
    API.run should start the server.
    """

    app = Flask(__name__)

    def run(self):
        self.app.run(debug=True)

    @app.route("/hello")
    def helloworld():
        return "Hellow World"

    @app.route("/device/<id>", methods=["DELETE"])
    def remove_device(id: str):
        utils.remove_device(id)
        return "", 204
