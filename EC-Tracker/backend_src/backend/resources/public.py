from flask_restful import Resource
from flask import jsonify
from app import db
from sqlalchemy import func
from models import EnergyRecord

class AverageEnergy(Resource):
    def get(self):
        average_consumption = db.session.query(func.avg(EnergyRecord.consumption)).scalar()
        return jsonify({"averageConsumption": average_consumption, "timePeriod": "all-time"}), 200

