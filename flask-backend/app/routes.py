from flask import Blueprint, jsonify
from .models import User

main = Blueprint("main", __name__)

@main.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "ok"})

@main.route("/message", methods=["GET"])
def message():
    return jsonify({"message": "Hello from Flask Backend!"})

@main.route("/users", methods=["GET"])
def get_users():
    try:
        users = User.query.all()
        return jsonify([{"id": u.id, "name": u.name} for u in users])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

