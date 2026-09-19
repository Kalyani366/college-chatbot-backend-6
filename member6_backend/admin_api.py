from flask import Blueprint, request, jsonify
import json
import os

admin_api = Blueprint("admin_api", __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "college_data.json")


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    return {}


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


college_data = load_data()


@admin_api.route("/api/admin/update", methods=["POST"])
def update_data():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No data provided"
        }), 400

    college_data.update(data)
    save_data(college_data)

    return jsonify({
        "message": "College information updated successfully",
        "data": college_data
    })


@admin_api.route("/api/admin/data", methods=["GET"])
def get_data():
    return jsonify({
        "data": college_data
    })