from extensions import db

class EnergyBenchmark(db.Model):
    __tablename__ = 'energy_benchmark'
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False, index=True)
    benchmark_value = db.Column(db.Float, nullable=False)
    
    city = db.relationship('City', back_populates='energy_benchmarks', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "city_id": self.city_id,
            "benchmark_value": self.benchmark_value
        }

    def __repr__(self):
        return f'<EnergyBenchmark {self.id} - City {self.city_id}>'
