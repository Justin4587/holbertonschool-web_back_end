#!/usr/bin/env python3
from crypt import methods
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth
app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def hello() -> str:
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def reg_user() -> str:
    try:
        email = request.form.get("email")
        password = request.form.get("password")
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password) is True:
        s_id = AUTH.create_session(email)
        resp = jsonify({
            "email": email,
            "message": "logged in"})
        resp.set_cookie("session_id", s_id)
        return resp
    else:
        abort(401)


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> None:
    """ logout function also destroy session """
    s_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(s_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")
    else:
        abort(403)


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile() -> str:
    """profile email"""
    s_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(s_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
