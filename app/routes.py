from flask import Blueprint, Flask, jsonify, request

from .database import get_all_table_data, get_user_all_table_data

app = Flask(__name__)

# Create a blueprint for the endpoints
data_blueprint = Blueprint('database', __name__)

@data_blueprint.route('/database', methods=['GET'])
def get_database():
    table = request.args.get('table')
    data = get_all_table_data(table)
    
    return jsonify(data)

@data_blueprint.route('/user/database', methods=['GET'])
def get_database_by_user():
    table = request.args.get('table')
    user_id = request.args.get('user_id')
    data = get_user_all_table_data(table_name=table, user_id=user_id)
    
    return jsonify(data)