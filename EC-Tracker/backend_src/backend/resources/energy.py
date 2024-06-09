from flask_restful import Resource, reqparse
from flask import jsonify
from app import db
from models import EnergyRecord

parser = reqparse.RequestParser()
parser.add_argument('user_id', type=int, required=True, help='User ID cannot be blank')
parser.add_argument('date', type=str, required=True, help='Date cannot be blank')
parser.add_argument('consumption', type=float, required=True, help='Consumption cannot be blank')

class EnergyList(Resource):
    def get(self):
        user_id = request.args.get('user_id')
        records = EnergyRecord.query.filter_by(user_id=user_id).all()
        return jsonify([model_to_dict(record) for record in records]), 200

    def post(self):
        data = parser.parse_args()
        new_record = EnergyRecord(user_id=data['user_id'], date=data['date'], consumption=data['consumption'])
        db.session.add(new_record)
        db.session.commit()
        
        return jsonify({"message": "Energy consumption recorded successfully"}), 201

class EnergyRecordResource(Resource):
    def get(self, record_id):
        record = EnergyRecord.query.get_or_404(record_id)
        return jsonify(model_to_dict(record)), 200

    def put(self, record_id):
        data = parser.parse_args()
        record = EnergyRecord.query.get_or_404(record_id)
        record.date = data['date']
        record.consumption = data['consumption']
        db.session.commit()
        return jsonify({"message": "Energy consumption record updated successfully"}), 200

    def delete(self, record_id):
        record = EnergyRecord.query.get_or_404(record_id)
        db.session.delete(record)
        db.session.commit()
        return jsonify({"message": "Energy consumption record deleted successfully"}), 200

