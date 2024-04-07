#!/usr/bin/python3
"""Main module"""


from flask import Flask, jsonify, make_response
from models import storage
import os
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(self):  # self argument is mandatory don't ask me why
    """Close the session"""
    storage.close()


@app.errorhandler(404)
def error_page(e):
    return make_response(jsonify(error="Not found"), 404)


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    if os.getenv('HBNB_API_HOST'):
        host = os.getenv('HBNB_API_HOST')
    if os.getenv('HBNB_API_PORT'):
        port = os.getenv('HBNB_API_PORT')
    app.run(host=host, port=port, threaded=True)
