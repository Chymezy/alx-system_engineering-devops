from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.energy_record_model import EnergyRecord
from models.user_model import User
from extensions import db

class EnergyRecordAPI(Resource):
    @jwt_required()
    def post(self):
        try:
            username = get_jwt_identity()
            user = User.query.filter_by(username=username).first()
            if not user:
                return {'message': 'User not found'}, 400
            data = request.get_json()
            energy_record = EnergyRecord(user_id=user.id, consumption=data['consumption'])
            db.session.add(energy_record)
            db.session.commit()
            return {'message': 'Energy record created'}, 201
        except Exception as e:
            return {'message': f'Internal server error: {str(e)}'}, 500

    @jwt_required()
    def get(self):
        try:
            username = get_jwt_identity()
            user = User.query.filter_by(username=username).first()
            if not user:
                return {'message': 'User not found'}, 400
            records = EnergyRecord.query.filter_by(user_id=user.id).all()
            return [record.to_dict() for record in records], 200
        except Exception as e:
            return {'message': f'Internal server error: {str(e)}'}, 500

    @jwt_required()
    def put(self, record_id):
        try:
            username = get_jwt_identity()
            user = User.query.filter_by(username=username).first()
            if not user:
                return {'message': 'User not found'}, 400
            data = request.get_json()
            record = EnergyRecord.query.get_or_404(record_id)
            if record.user_id != user.id:
                return {'message': 'Unauthorized'}, 401
            record.consumption = data['consumption']
            db.session.commit()
            return {'message': 'Energy record updated'}, 200
        except Exception as e:
            return {'message': f'Internal server error: {str(e)}'}, 500

    @jwt_required()
    def delete(self, record_id):
        try:
            username = get_jwt_identity()
            user = User.query.filter_by(username=username).first()
            if not user:
                return {'message': 'User not found'}, 400
            record = EnergyRecord.query.get_or_404(record_id)
            if record.user_id != user.id:
                return {'message': 'Unauthorized'}, 401
            db.session.delete(record)
            db.session.commit()
            return {'message': 'Energy record deleted'}, 200
        except Exception as e:
            return {'message': f'Internal server error: {str(e)}'}, 500
