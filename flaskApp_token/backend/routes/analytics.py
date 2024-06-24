from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.models.analytics import Analytics
from backend.utils.db import db


# Importance: Manages analytics data for users

class AnalyticsAPI(Resource):
    # Define GET method for retrieving analytics
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        analytics = Analytics.query.filter_by(user_id=user_id).all()
        return [analytic.to_dict() for analytic in analytics], 200

    # Define POST method for creating analytics
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.get_json()
        analytics = Analytics(user_id=user_id, data=data)
        db.session.add(analytics)
        db.session.commit()
        return {'message': 'Analytics created'}, 201

