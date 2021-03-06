#!/usr/bin/env python3
from crypt import methods
from flask import Flask, jsonify, request, abort
from auth import Auth

app = Flask(__name__)
auth = Auth()


@app.route("/", methods=["GET"])
def hello() -> str:
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def reg_user() -> str:
    try:
        email = request.form.get("email")
        password = request.form.get("password")
        auth.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})

@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    try:
        email = request.form.get("email")
    except:
        return
    try:
        password = request.form.get("password")
    except:
        return
    if auth.valid_login(email, password) is True:
        s_id = auth.create_session(email)
        resp = jsonify({"email": email,
        "message": "logged in"})
        resp.set_cookie("session_id", s_id)
        return resp
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
