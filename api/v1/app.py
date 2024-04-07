#!/usr/bin/python3
"""Main module"""


from flask import Flask
from models import storage
import os
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close():
    """Close the session"""
    storage.close()




if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST')
    port = os.getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)


# if __name__ == '__main__':
#     host = '0.0.0.0'
#     port = 5000
#     if os.getenv('HBNB_API_HOST'):
#         host = os.getenv('HBNB_API_HOST')
#     if os.getenv('HBNB_API_PORT'):
#         port = os.getenv('HBNB_API_PORT')
#     app.run(host=host, port=port, threaded=True)
