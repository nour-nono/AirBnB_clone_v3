#!/usr/bin/python3
"""api status"""
from models import storage
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status_all_obj():
    """Return status for all obj"""
    dd = {"amenities": storage.count("Amenity"),
          "cities": storage.count("City"),
          "places": storage.count("Place"),
          "reviews": storage.count("Review"),
          "states": storage.count("State"),
          "users": storage.count("User")}
    return jsonify(dd)
