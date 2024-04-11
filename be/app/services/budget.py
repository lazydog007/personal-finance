import uuid
from flask import Blueprint, request, jsonify
import sqlite3
from datetime import datetime

import pandas as pd

from app.database import create_connection, search_in_column, update_row_by_id

DATABASE_FILE = "data/personal_finance_data.db"

budget_blueprint = Blueprint("budgets", __name__)

COLUMNS = ["budget_id", "user_id", "category_id", "amount", "start_date", "end_date"]


@budget_blueprint.route("/budget", methods=["POST"])
def add_budget():
    try:
        data = request.get_json()
        budget_id = str(uuid.uuid4())
        user_id = data.get("user_id")
        category_id = data.get("category_id")
        amount = data.get("amount")
        start_date = data.get("start_date")
        end_date = data.get("end_date")

        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO budgets(budget_id, user_id, category_id, amount, start_date, end_date)
            VALUES(%s, %s, %s, %s, %s, %s)
        """,
            (budget_id, user_id, category_id, amount, start_date, end_date),
        )

        conn.commit()
        conn.close()

        return jsonify({"message": f"Budget {budget_id} added successfully"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500


# Get all budgets users from the database
@budget_blueprint.route("/budget/user/<user_id>", methods=["GET"])
def get_budget_user_id(user_id):
    try:
        budgets = search_in_column("budgets", "user_id", user_id)
        df = pd.DataFrame(budgets, columns=COLUMNS)
        budgets_df = df.to_dict("records")

        return jsonify(budgets_df), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@budget_blueprint.route("/budget/<budget_id>", methods=["GET"])
def get_budget(budget_id):
    try:
        budgets = search_in_column("budgets", "budget_id", budget_id)
        df = pd.DataFrame(budgets, columns=COLUMNS)
        budgets_df = df.to_dict("records")

        return jsonify(budgets_df[0]), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@budget_blueprint.route("/budget/<budget_id>", methods=["PUT"])
def update_budget(budget_id):
    try:
        data = request.get_json()

        user_id = data.get("user_id")
        category_id = data.get("category_id")
        amount = data.get("amount")
        start_date = data.get("start_date")
        end_date = data.get("end_date")

        try:
            current_budgets = search_in_column("budgets", "budget_id", budget_id)

            # check if the budget exists
            if current_budgets:
                df = pd.DataFrame(current_budgets, columns=COLUMNS)
                current_budgets_df = df.to_dict("records")
                if current_budgets_df[0]["user_id"] != user_id:
                    return (
                        jsonify(
                            {
                                "message": f"User {user_id} not authorized to update this budget"
                            }
                        ),
                        403,
                    )
        except Exception as e:
            return jsonify({"message": f"Transaction {budget_id} not found"}), 404

        updated_details = {
            "category_id": category_id,
            "amount": amount,
            "start_date": start_date,
            "end_date": end_date,
        }

        # Remove None values from the updated_details
        updated_details = {k: v for k, v in updated_details.items() if v is not None}

        update_row_by_id("budgets", "budget_id", budget_id, updated_details)

        return (
            jsonify({"message": f"Transaction {budget_id} updated successfully"}),
            200,
        )
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@budget_blueprint.route("/budget/<budget_id>", methods=["DELETE"])
def delete_budget(budget_id):
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM budgets WHERE budget_id = ?", (budget_id,))

        conn.commit()
        conn.close()

        return jsonify({"message": "Budget deleted successfully"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
