# Transaction Service
from flask import Blueprint, Flask, jsonify, request

from app.database import get_all_table_data, get_user_all_table_data

app = Flask(__name__)
transaction_blueprint = Blueprint("transaction", __name__)


@transaction_blueprint.route("/transaction", methods=["POST"])
def add_transaction():
    # Implementation here
    print("chill")


@transaction_blueprint.route("/transaction", methods=["GET"])
def get_transactions():
    # Implementation here
    print("chill")


@transaction_blueprint.route("/transaction/<transaction_id>", methods=["PUT"])
def update_transaction(transaction_id):
    # Implementation here
    print("chill")


@transaction_blueprint.route("/transaction/<transaction_id>", methods=["DELETE"])
def delete_transaction(transaction_id):
    # Implementation here
    print("chill")
