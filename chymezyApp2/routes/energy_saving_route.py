from models.energy_saving_model import EnergySaving
from extensions import db
from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required

class EnergySavingAPI(Resource):
    @jwt_required()
    def get(self, saving_id=None):
        try:
            if saving_id:
                saving = EnergySaving.query.get(saving_id)
                if not saving:
                    return {'message': 'Energy saving not found'}, 404
                return jsonify(saving.to_dict())
            else:
                savings = EnergySaving.query.all()
                return jsonify([saving.to_dict() for saving in savings])

        except Exception as e:
            return {'message': f'Internal server error: {str(e)}'}, 500

    @jwt_required()
    def post(self):
        try:
            data = request.get_json()
            saving = EnergySaving(
                user_id=data['user_id'],
                energy_record_id=data['energy_record_id'],
                saved_kwh=data['saved_kwh'],
                money_saved=data['money_saved'],
                calculation_date=data['calculation_date']
            )
            db.session.add(saving)
            db.session.commit()
            return {'message': 'Energy saving created'}, 201

        except Exception as e:
            return {'message': f'Internal server error: {str(e)}'}, 500

    @jwt_required()
    def put(self, saving_id):
        try:
            data = request.get_json()
            saving = EnergySaving.query.get(saving_id)
            if not saving:
                return {'message': 'Energy saving not found'}, 404

            saving.user_id = data.get('user_id', saving.user_id)
            saving.energy_record_id = data.get('energy_record_id', saving.energy_record_id)
            saving.saved_kwh = data.get('saved_kwh', saving.saved_kwh)
            saving.money_saved = data.get('money_saved', saving.money_saved)
            saving.calculation_date = data.get('calculation_date', saving.calculation_date)
            db.session.commit()
            return {'message': 'Energy saving updated'}, 200

        except Exception as e:
            return {'message': f'Internal server error: {str(e)}'}, 500

    @jwt_required()
    def delete(self, saving_id):
        try:
            saving = EnergySaving.query.get(saving_id)
            if not saving:
                return {'message': 'Energy saving not found'}, 404

            db.session.delete(saving)
            db.session.commit()
            return {'message': 'Energy saving deleted'}, 200

        except Exception as e:
            return {'message': f'Internal server error: {str(e)}'}, 500
