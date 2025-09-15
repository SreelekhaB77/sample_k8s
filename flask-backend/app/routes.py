from flask import Blueprint, jsonify
from .models import User

main = Blueprint("main", __name__)

@main.route("/api/message", methods=["GET"])
def message():
    return jsonify({"message": "Hello from Flask Backend!"})

@main.route("/api/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name} for u in users])
