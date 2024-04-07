#!/usr/bin/python3
"""api status"""
from models import storage
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status_all_obj():
	"""Return status for all obj"""
	classes = ["Amenity", "City", "Place", "Review", "State", "User"]
	dd = {}
	for c in classes:
		dd[c] = storage.count(c)
	return jsonify(dd)
