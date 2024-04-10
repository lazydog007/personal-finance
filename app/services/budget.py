# Transaction Service
from flask import Blueprint, Flask

app = Flask(__name__)
budget_blueprint = Blueprint("transactions", __name__)


@budget_blueprint.route("/budget", methods=["POST"])
def add_budget():
    # Implementation here
    print("chill")


@budget_blueprint.route("/budget", methods=["GET"])
def get_budgets():
    # Implementation here
    print("chill")


@budget_blueprint.route("/budget/<budget_id>", methods=["PUT"])
def update_budget(budget_id):
    # Implementation here
    print("chill")


@budget_blueprint.route("/budget/<budget_id>", methods=["DELETE"])
def delete_budget(budget_id):
    # Implementation here
    print("chill")


@budget_blueprint.route("/budgets", methods=["GET"])
def get_budgets():
    # Implementation here
    print("chill")
