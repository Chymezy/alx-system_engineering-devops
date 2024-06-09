from flask import Blueprint, jsonify
from backend.models.analytics import Analytics

bp = Blueprint('analytics', __name__, url_prefix='/api/analytics')

@bp.route('/', methods=['GET'])
def get_analytics():
    analytics = Analytics.query.all()
    return jsonify([{
        "id": analytic.id,
        "total_energy_consumed": analytic.total_energy_consumed,
        "timestamp": analytic.timestamp
    } for analytic in analytics]), 200

