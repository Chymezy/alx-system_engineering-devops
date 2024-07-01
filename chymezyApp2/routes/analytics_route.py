from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.analytics_model import Analytics
from models.user_model import User
from extensions import db

class AnalyticsAPI(Resource):
    @jwt_required()
    def post(self):
        try:
            username = get_jwt_identity()
            user = User.query.filter_by(username=username).first()
            if not user:
                return {'message': 'User not found'}, 400
            
            data = request.get_json()
            # Set user_id instead of username
            analytics = Analytics(user_id=user.id, data=data['data'])
            db.session.add(analytics)
            db.session.commit()
            
            return {'message': 'Analytics record created'}, 201
        except Exception as e:
            return {'message': f'Internal server error: {str(e)}'}, 500

    @jwt_required()
    def get(self):
        try:
            username = get_jwt_identity()
            user = User.query.filter_by(username=username).first()
            if not user:
                return {'message': 'User not found'}, 400
            
            records = Analytics.query.filter_by(user_id=user.id).all()
            return [record.to_dict() for record in records], 200
        except Exception as e:
            return {'message': f'Internal server error: {str(e)}'}, 500
