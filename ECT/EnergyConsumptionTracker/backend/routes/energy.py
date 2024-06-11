from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.models.energy_record import EnergyRecord
from backend.utils.db import db

# Importance: Manages user energy records.

class EnergyAPI(Resource):
    # Define POST method for adding an energy record
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.get_json()
        energy_record = EnergyRecord(user_id=user_id, consumption=data['consumption'])
        db.session.add(energy_record)
        db.session.commit()
        return {'message': 'Energy record created'}, 201

    # Define GET method for retrieving energy records
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        records = EnergyRecord.query.filter_by(user_id=user_id).all()
        return [record.to_dict() for record in records], 200

    # Define PUT method for updating an energy record
    @jwt_required()
    def put(self, record_id):
        data = request.get_json()
        record = EnergyRecord.query.get_or_404(record_id)
        if record.user_id != get_jwt_identity():
            return {'message': 'Unauthorized'}, 401
        record.consumption = data['consumption']
        db.session.commit()
        return {'message': 'Energy record updated'}, 200

    # Define DELETE method for deleting an energy record
    @jwt_required()
    def delete(self, record_id):
        record = EnergyRecord.query.get_or_404(record_id)
        if record.user_id != get_jwt_identity():
            return {'message': 'Unauthorized'}, 401
        db.session.delete(record)
        db.session.commit()
        return {'message': 'Energy record deleted'}, 200

