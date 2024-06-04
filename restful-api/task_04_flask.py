#!/usr/bin/python3
"""
    Python script to Develop a Simple API
    using Python with Flask
"""
from flask import Flask, jsonify, request


app = Flask(__name__)

users = {}


@ app.route("/")
def home():
    """
    Function to handle the "/" route.

    Returns:
        A string with message "Welcome to the Flask API!"
    """
    return "Welcome to the Flask API!"


@ app.route("/status")
def status():
    """
    Function to handle the "/status" route.

    Returns:
        A string with message "OK"
    """
    return "OK"


@ app.route("/data")
def data():
    """
    Function to handle the "/data" route.

    Returns:
        A JSON response wich is the list
        of existing user(s) name.
    """
    return (jsonify(list(users.keys())))


@ app.route("/users/<username>")
def get_user(username):
    """
    Function to handle the "/users/<username>" route.

    Returns:
        if user exist, return the corresponding user data.
        If not, send an error message.
    """
    user = users.get(username)
    if user:
        return (jsonify(user))
    else:
        return (jsonify({"error": "User not found"}), 404)


@ app.route("/add_user", methods=["POST"])
def add_user():
    """
    Function to add a new user.

    Returns:
        Add a new user to the users dictionary.
    """
    user_data = request.get_json()
    username = user_data["username"]
    if not username:
        return (jsonify({"error": "Username is required"}), 400)
    users[username] = user_data
    return (jsonify({"message": "User added", "user": user_data}), 201)


if __name__ == "__main__":
    app.run()
