from models.energy_benchmark_model import EnergyBenchmark
from extensions import db
from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required

class EnergyBenchmarkAPI(Resource):
    @jwt_required()
    def get(self, benchmark_id=None):
        try:
            if benchmark_id:
                benchmark = EnergyBenchmark.query.get(benchmark_id)
                if not benchmark:
                    return {'message': 'Energy benchmark not found'}, 404
                return jsonify(benchmark.to_dict())
            else:
                benchmarks = EnergyBenchmark.query.all()
                return jsonify([benchmark.to_dict() for benchmark in benchmarks])

        except Exception as e:
            return {'message': f'Internal server error: {str(e)}'}, 500

    @jwt_required()
    def post(self):
        try:
            data = request.get_json()
            benchmark = EnergyBenchmark(
                city_id=data['city_id'],
                benchmark_value=data['benchmark_value']
            )
            db.session.add(benchmark)
            db.session.commit()
            return {'message': 'Energy benchmark created'}, 201

        except Exception as e:
            return {'message': f'Internal server error: {str(e)}'}, 500

    @jwt_required()
    def put(self, benchmark_id):
        try:
            data = request.get_json()
            benchmark = EnergyBenchmark.query.get(benchmark_id)
            if not benchmark:
                return {'message': 'Energy benchmark not found'}, 404

            benchmark.city_id = data.get('city_id', benchmark.city_id)
            benchmark.benchmark_value = data.get('benchmark_value', benchmark.benchmark_value)
            db.session.commit()
            return {'message': 'Energy benchmark updated'}, 200

        except Exception as e:
            return {'message': f'Internal server error: {str(e)}'}, 500

    @jwt_required()
    def delete(self, benchmark_id):
        try:
            benchmark = EnergyBenchmark.query.get(benchmark_id)
            if not benchmark:
                return {'message': 'Energy benchmark not found'}, 404

            db.session.delete(benchmark)
            db.session.commit()
            return {'message': 'Energy benchmark deleted'}, 200

        except Exception as e:
            return {'message': f'Internal server error: {str(e)}'}, 500
