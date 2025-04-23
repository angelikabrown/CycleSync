
#from flask import Blueprint
from flask import request, jsonify
from models import db, User, Data


def init_routes(app):
    @app.route('/', methods=['GET'])
    def hi():
        return 'Hello, World!'
    @app.route('/users', methods=['GET'])
    def get_users():
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])

    @app.route('/users/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        user = User.query.get_or_404(user_id)
        return jsonify(user.to_dict())

    @app.route('/users', methods=['POST'])
    def create_user():
        data = request.get_json()
        print("data received:", data)
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201

    @app.route('/users/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        
        if 'username' in data:
            user.username = data['username']
        if 'email' in data:
            user.email = data['email']
            
        db.session.commit()
        return jsonify(user.to_dict())

    @app.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204
    

    @app.route('/data', methods=['GET'])
    def get_data():
        data = Data.query.all()
        return jsonify([data.to_dict() for data in data])



#define the blueprint in routes.py 
# #register it in __init__.py
#rt = Blueprint('routes', __name__)