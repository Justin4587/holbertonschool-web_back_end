#!/usr/bin/env python3
""" views flas session auth do I need more
words
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login():
    """ POST method for login
    maybe here
    """
    email = request.form.get("email")
    pswd = request.form.get("password")

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not pswd:
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    for use in user:
        if not use.is_valid_password(pswd):
            return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    name = getenv("SESSION_NAME")
    s_id = auth.create_session(user[0].id)
    response = jsonify(user[0].to_json())
    response.set_cookie(name, s_id)
    return response
