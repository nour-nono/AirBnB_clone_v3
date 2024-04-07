#!/usr/bin/python3
"""api status"""
import models
from models import storage
from models.base_model import BaseModel
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status_all_obj():
    """Return status for all obj"""
    classes = {'states': State, 'users': User,
               'amenities': Amenity, 'cities': City,
               'places': Place, 'reviews': Review}
    dd = {}
    for c in classes:
        dd[c] = storage.count(c)
    return jsonify(dd)
