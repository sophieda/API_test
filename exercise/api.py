from flask import Flask, request
from threading import Thread
import uuid

import utils
from device import Device
from exercise.errors import ErrorDeviceAlreadyExists, ErrorDeviceNotFound


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

    @app.route("/device", methods=["POST"])
    def add_device():
        try:
            data = request.json
            # create unique id
            unique_id = str(uuid.uuid4())
            device = Device(id=unique_id, **data)
            try:
                utils.create_device(device)
                return unique_id, 200

            except ErrorDeviceAlreadyExists:
                return "", 403
        except:
            return "", 500

    @app.route("/device/<id>", methods=["DELETE"])
    def remove_device(id: str):
        try:
            try:
                utils.remove_device(id)
                return f"delete : {id}", 204

            except ErrorDeviceNotFound:
                return "", 404
        except:
            return "", 500
