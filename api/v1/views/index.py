#!/usr/bin/python3
"""Index module"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status_obj():
	"""Return status"""
	return jsonify(status="OK")
