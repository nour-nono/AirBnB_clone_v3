#!/usr/bin/python3
"""Main module"""
from flask import Flask
import os
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close():
    """Close the session"""
    storage.close()


if __name__ == '__main__':
    if os.getenv('HBNB_API_HOST') and os.getenv('HBNB_API_PORT'):
        app.run(host=os.getenv('HBNB_API_HOST'),
                port=os.getenv('HBNB_API_PORT'), threaded=True)
    else:
        app.run(host='0.0.0.0', port=5000, threaded=True)
