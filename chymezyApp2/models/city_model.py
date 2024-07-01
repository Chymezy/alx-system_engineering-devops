from extensions import db

class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    cost_of_electricity = db.Column(db.Float, nullable=False)
    cost_of_fuel = db.Column(db.Float, nullable=False)
    electricity_availability = db.Column(db.Float, nullable=False)
    
    users = db.relationship('User', back_populates='city', lazy=True)
    energy_benchmarks = db.relationship('EnergyBenchmark', back_populates='city', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country,
            "cost_of_electricity": self.cost_of_electricity,
            "cost_of_fuel": self.cost_of_fuel,
            "electricity_availability": self.electricity_availability
        }

    def __repr__(self):
        return f'<City {self.name} - {self.country}>'
