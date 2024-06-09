from flask import Blueprint, request, jsonify
from backend.models.user import User
from backend.utils.db import db

bp = Blueprint('user', __name__, url_prefix='/api/users')

@bp.route('/', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=data['password']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "userId": new_user.id}), 201

@bp.route('/', methods=['GET'])
def get_user():
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)
    if user:
        return jsonify({
            "userId": user.id,
            "username": user.username,
            "email": user.email,
            "created_at": user.created_at
        }), 200
    return jsonify({"error": "User not found"}), 404

