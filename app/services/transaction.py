# Transaction Service
from datetime import datetime
import uuid
from flask import Blueprint, request, jsonify
from app.database import (
    create_connection,
    delete_row_by_id,
    get_all_table_data,
    get_user_all_table_data,
    search_in_column,
    update_row_by_id,
)
import pandas as pd

transaction_blueprint = Blueprint("transaction", __name__)

COLUMNS = [
    "transaction_id",
    "account_id",
    "user_id",
    "transaction_type",
    "amount",
    "category_id",
    "transaction_date",
    "description",
    "created_at",
]


@transaction_blueprint.route("/transaction", methods=["POST"])
def add_transaction():
    try:
        body = request.get_json()

        transaction_id = str(
            uuid.uuid4()
        )  # Generate a unique transaction ID and convert it to a string
        account_id = body.get("account_id")
        user_id = body.get("user_id")
        transaction_type = body.get("transaction_type")
        amount = body.get("amount")
        category_id = body.get("category_id")
        transaction_date = body.get("transaction_date")
        description = body.get("description")
        created_at = datetime.now()

        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO transactions(transaction_id, account_id, user_id, transaction_type, amount, category_id, transaction_date, description, created_at)
            VALUES(?,?,?,?,?,?,?,?,?)
        """,
            (
                transaction_id,
                account_id,
                user_id,
                transaction_type,
                amount,
                category_id,
                transaction_date,
                description,
                created_at,
            ),
        )

        conn.commit()
        conn.close()

        return (
            jsonify({"message": f"Transaction {transaction_id} added successfully"}),
            201,
        )
    except Exception as e:
        return jsonify({"message": str(e)}), 500


# Get all transactions from the database
@transaction_blueprint.route("/transaction", methods=["GET"])
def get_transactions():
    try:
        transactions = get_all_table_data("transactions")
        df = pd.DataFrame(transactions, columns=COLUMNS)
        transactions_df = df.to_dict("records")

        return jsonify(transactions_df), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


# Get a specific transaction based on its transaction_id from the database
@transaction_blueprint.route("/transaction/<transaction_id>", methods=["GET"])
def get_transaction(transaction_id):
    try:
        transactions = search_in_column(
            "transactions", "transaction_id", transaction_id
        )
        df = pd.DataFrame(transactions, columns=COLUMNS)
        transactions_df = df.to_dict("records")

        return jsonify(transactions_df[0]), 200
    except Exception as e:
        return jsonify({"message": f"Transaction {transaction_id} not found"}), 404


@transaction_blueprint.route("/transaction/<transaction_id>", methods=["PUT"])
def update_transaction(transaction_id):
    try:

        body = request.get_json()

        user_id = body.get("user_id")
        account_id = body.get("account_id")  # required
        transaction_type = body.get("transaction_type")
        amount = body.get("amount")
        category_id = body.get("category_id")  # required
        transaction_date = body.get("transaction_date")
        description = body.get("description")

        try:
            current_transactions = search_in_column(
                "transactions", "transaction_id", transaction_id
            )

            # check if the transaction exists
            if current_transactions:
                df = pd.DataFrame(current_transactions, columns=COLUMNS)
                current_transactions_df = df.to_dict("records")
                if current_transactions_df[0]["user_id"] != user_id:
                    return (
                        jsonify(
                            {
                                "message": f"User {user_id} not authorized to update this transaction"
                            }
                        ),
                        403,
                    )
        except Exception as e:
            return jsonify({"message": f"Transaction {transaction_id} not found"}), 404

        updated_details = {
            "account_id": account_id,
            "transaction_type": transaction_type,
            "amount": amount,
            "category_id": category_id,
            "transaction_date": transaction_date,
            "description": description,
        }

        update_row_by_id(
            "transactions", "transaction_id", transaction_id, updated_details
        )

        return (
            jsonify({"message": f"Transaction {transaction_id} updated successfully"}),
            200,
        )
    except Exception as e:
        return (
            jsonify({"message": f"Failed to update transaction {transaction_id}"}),
            500,
        )


@transaction_blueprint.route("/transaction/<transaction_id>", methods=["DELETE"])
def delete_transaction(transaction_id):
    delete_row_by_id("transactions", "transaction_id", transaction_id)
    return jsonify({"message": "Transaction deleted successfully"}), 200
