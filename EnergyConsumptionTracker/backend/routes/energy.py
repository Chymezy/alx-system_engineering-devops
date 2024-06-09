from flask import Blueprint, request, jsonify
from backend.models.energy_record import EnergyRecord
from backend.utils.db import db

bp = Blueprint('energy', __name__, url_prefix='/api/energy')

@bp.route('/', methods=['POST'])
def add_energy_record():
    data = request.get_json()
    record = EnergyRecord(
        user_id=data['user_id'],
        energy_consumed=data['energy_consumed']
    )
    db.session.add(record)
    db.session.commit()
    return jsonify({"message": "Energy record added", "recordId": record.id}), 201

@bp.route('/', methods=['GET'])
def get_energy_records():
    records = EnergyRecord.query.all()
    return jsonify([{
        "id": record.id,
        "user_id": record.user_id,
        "energy_consumed": record.energy_consumed,
        "timestamp": record.timestamp
    } for record in records]), 200

@bp.route('/<int:record_id>', methods=['GET'])
def get_energy_record(record_id):
    record = EnergyRecord.query.get(record_id)
    if record:
        return jsonify({
            "id": record.id,
            "user_id": record.user_id,
            "energy_consumed": record.energy_consumed,
            "timestamp": record.timestamp
        }), 200
    return jsonify({"error": "Record not found"}), 404

@bp.route('/<int:record_id>', methods=['PUT'])
def update_energy_record(record_id):
    record = EnergyRecord.query.get(record_id)
    if not record:
        return jsonify({"error": "Record not found"}), 404
    data = request.get_json()
    record.energy_consumed = data.get('energy_consumed', record.energy_consumed)
    db.session.commit()
    return jsonify({"message": "Energy record updated"}), 200

@bp.route('/<int:record_id>', methods=['DELETE'])
def delete_energy_record(record_id):
    record = EnergyRecord.query.get(record_id)
    if not record:
        return jsonify({"error": "Record not found"}), 404
    db.session.delete(record)
    db.session.commit()
    return jsonify({"message": "Energy record deleted"}), 200

