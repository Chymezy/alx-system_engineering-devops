from flask_restful import Resource
from flask_jwt_extended import jwt_required
from models import Analytics

class AnalyticsResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        analytics = Analytics.query.filter_by(user_id=user_id).all()
        return [analytic.to_dict() for analytic in analytics], 200

