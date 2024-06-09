from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import db, Analytics

analytics_bp = Blueprint('analytics_bp', __name__)

@analytics_bp.route('/api/analytics', methods=['GET'])
@jwt_required()
def get_analytics():
    user_id = get_jwt_identity()
    analytics_data = Analytics.query.filter_by(user_id=user_id).all()

    return jsonify([
        {
            'id': data.id,
            'average_consumption': data.average_consumption,
            'time_period': data.time_period
        } for data in analytics_data
    ]), 200

