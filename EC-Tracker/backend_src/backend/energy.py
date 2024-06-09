from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import db, EnergyRecord

energy_bp = Blueprint('energy_bp', __name__)

@energy_bp.route('/api/energy', methods=['POST'])
@jwt_required()
def add_energy_record():
    data = request.get_json()
    user_id = get_jwt_identity()
    date = data.get('date')
    consumption = data.get('consumption')

    if not date or not consumption:
        return jsonify({'error': 'Missing required fields'}), 400

    new_record = EnergyRecord(user_id=user_id, date=date, consumption=consumption)
    db.session.add(new_record)
    db.session.commit()

    return jsonify({'message': 'Energy consumption recorded successfully', 'recordId': new_record.id}), 201

@energy_bp.route('/api/energy', methods=['GET'])
@jwt_required()
def get_energy_records():
    user_id = get_jwt_identity()
    records = EnergyRecord.query.filter_by(user_id=user_id).all()

    return jsonify([
        {'recordId': record.id, 'date': record.date, 'consumption': record.consumption}
        for record in records
    ]), 200

@energy_bp.route('/api/energy/<int:record_id>', methods=['GET'])
@jwt_required()
def get_energy_record(record_id):
    user_id = get_jwt_identity()
    record = EnergyRecord.query.filter_by(user_id=user_id, id=record_id).first()

    if not record:
        return jsonify({'error': 'Record not found'}), 404

    return jsonify({
        'recordId': record.id,
        'date': record.date,
        'consumption': record.consumption
    }), 200

@energy_bp.route('/api/energy/<int:record_id>', methods=['PUT'])
@jwt_required()
def update_energy_record(record_id):
    data = request.get_json()
    user_id = get_jwt_identity()
    record = EnergyRecord.query.filter_by(user_id=user_id, id=record_id).first()

    if not record:
        return jsonify({'error': 'Record not found'}), 404

    record.date = data.get('date', record.date)
    record.consumption = data.get('consumption', record.consumption)
    db.session.commit()

    return jsonify({'message': 'Energy consumption record updated successfully'}), 200

@energy_bp.route('/api/energy/<int:record_id>', methods=['DELETE'])
@jwt_required()
def delete_energy_record(record_id):
    user_id = get_jwt_identity()
    record = EnergyRecord.query.filter_by(user_id=user_id, id=record_id).first()

    if not record:
        return jsonify({'error': 'Record not found'}), 404

    db.session.delete(record)
    db.session.commit()

    return jsonify({'message': 'Energy consumption record deleted successfully'}), 200

