from flask import Blueprint, jsonify
from dataclasses import dataclass

api = Blueprint('api', __name__, url_prefix='/api/v1')


@dataclass
class Todo:
    name: str


@api.route('/health')
def health():
    return jsonify({"status": "ok"})


@api.route('/todos')
def create():
    pass
