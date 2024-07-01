from models.city_model import City
from extensions import db
from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required

class CityAPI(Resource):
    @jwt_required()
    def get(self, city_id=None):
        try:
            if city_id:
                city = City.query.get(city_id)
                if not city:
                    return {'message': 'City not found'}, 404
                return jsonify(city.to_dict())
            else:
                cities = City.query.all()
                return jsonify([city.to_dict() for city in cities])

        except Exception as e:
            return {'message': f'Internal server error: {str(e)}'}, 500

    @jwt_required()
    def post(self):
        try:
            data = request.get_json()
            city = City(
                name=data['name'],
                country=data['country'],
                cost_of_electricity=data['cost_of_electricity'],
                cost_of_fuel=data['cost_of_fuel'],
                electricity_availability=data['electricity_availability']
            )
            db.session.add(city)
            db.session.commit()
            return {'message': 'City created'}, 201

        except Exception as e:
            return {'message': f'Internal server error: {str(e)}'}, 500

    @jwt_required()
    def put(self, city_id):
        try:
            data = request.get_json()
            city = City.query.get(city_id)
            if not city:
                return {'message': 'City not found'}, 404

            city.name = data.get('name', city.name)
            city.country = data.get('country', city.country)
            city.cost_of_electricity = data.get('cost_of_electricity', city.cost_of_electricity)
            city.cost_of_fuel = data.get('cost_of_fuel', city.cost_of_fuel)
            city.electricity_availability = data.get('electricity_availability', city.electricity_availability)
            db.session.commit()
            return {'message': 'City updated'}, 200

        except Exception as e:
            return {'message': f'Internal server error: {str(e)}'}, 500

    @jwt_required()
    def delete(self, city_id):
        try:
            city = City.query.get(city_id)
            if not city:
                return {'message': 'City not found'}, 404

            db.session.delete(city)
            db.session.commit()
            return {'message': 'City deleted'}, 200

        except Exception as e:
            return {'message': f'Internal server error: {str(e)}'}, 500
