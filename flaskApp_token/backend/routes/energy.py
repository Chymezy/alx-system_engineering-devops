# from flask import request
# from flask_restful import Resource
# from flask_jwt_extended import jwt_required, get_jwt_identity
# from backend.models.energy_record import EnergyRecord
# from backend.utils.db import db
# from backend.utils.to_dict import model_to_dict


# # Importance: Manages user energy records.

# class EnergyAPI(Resource):
#     # Define POST method for adding an energy record
#     @jwt_required()
#     def post(self):
#         user_id = get_jwt_identity()
#         data = request.get_json()
#         energy_record = EnergyRecord(user_id=user_id, consumption=data['consumption'])
#         db.session.add(energy_record)
#         db.session.commit()
#         return {'message': 'Energy record created'}, 201

#     # Define GET method for retrieving energy records
#     @jwt_required()
#     def get(self):
#         user_id = get_jwt_identity()
#         records = EnergyRecord.query.filter_by(user_id=user_id).all()
#         return [record.to_dict() for record in records], 200

#     # Define PUT method for updating an energy record
#     @jwt_required()
#     def put(self, record_id):
#         data = request.get_json()
#         record = EnergyRecord.query.get_or_404(record_id)
#         if record.user_id != get_jwt_identity():
#             return {'message': 'Unauthorized'}, 401
#         record.consumption = data['consumption']
#         db.session.commit()
#         return {'message': 'Energy record updated'}, 200

#     # Define DELETE method for deleting an energy record
#     @jwt_required()
#     def delete(self, record_id):
#         record = EnergyRecord.query.get_or_404(record_id)
#         if record.user_id != get_jwt_identity():
#             return {'message': 'Unauthorized'}, 401
#         db.session.delete(record)
#         db.session.commit()
#         return {'message': 'Energy record deleted'}, 200

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.models.energy_record import EnergyRecord
from backend.utils.db import db

energy_bp = Blueprint('energy_bp', __name__)

@energy_bp.route('/api/energy', methods=['POST'])
@jwt_required()
def add_energy_record():
    current_user = get_jwt_identity()
    data = request.get_json()
    
    try:
        energy_record = EnergyRecord(
            user_id=current_user['id'],
            energy_consumption=data['energy_consumption'],
            timestamp=data['timestamp']
        )
        db.session.add(energy_record)
        db.session.commit()
        return jsonify({"msg": "Energy record added", "data": energy_record.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": "Failed to add energy record", "error": str(e)}), 500
    finally:
        db.session.close()

@energy_bp.route('/api/energy', methods=['GET'])
@jwt_required()
def get_energy_records():
    current_user = get_jwt_identity()
    try:
        energy_records = EnergyRecord.query.filter_by(user_id=current_user['id']).all()
        return jsonify([record.to_dict() for record in energy_records]), 200
    except Exception as e:
        return jsonify({"msg": "Failed to fetch energy records", "error": str(e)}), 500
