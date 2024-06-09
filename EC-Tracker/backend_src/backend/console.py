import cmd
from datetime import datetime
from .models import db, User, EnergyRecord, Analytics
from app import app

class Console(cmd.Cmd):
    intro = 'Welcome to the Energy Consumption Tracker console. Type help or ? to list commands.\n'
    prompt = '(tracker) '

    def do_create_user(self, arg):
        'Create a new user: create_user username email password'
        args = arg.split()
        if len(args) != 3:
            print("Usage: create_user username email password")
            return
        username, email, password = args
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        print(f"User {username} created with id {user.id}")

    def do_get_user(self, arg):
        'Get user details by username: get_user username'
        args = arg.split()
        if len(args) != 1:
            print("Usage: get_user username")
            return
        username = args[0]
        user = User.query.filter_by(username=username).first()
        if user:
            print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}, Created at: {user.created_at}, Updated at: {user.updated_at}")
        else:
            print("User not found")

    def do_create_energy(self, arg):
        'Create an energy record: create_energy user_id date consumption'
        args = arg.split()
        if len(args) != 3:
            print("Usage: create_energy user_id date consumption")
            return
        user_id, date_str, consumption = args
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        energy = EnergyRecord(user_id=user_id, date=date, consumption=float(consumption))
        db.session.add(energy)
        db.session.commit()
        print(f"Energy record created with id {energy.id}")

    def do_get_energy(self, arg):
        'Get energy records by user_id: get_energy user_id'
        args = arg.split()
        if len(args) != 1:
            print("Usage: get_energy user_id")
            return
        user_id = args[0]
        records = EnergyRecord.query.filter_by(user_id=user_id).all()
        for record in records:
            print(f"ID: {record.id}, Date: {record.date}, Consumption: {record.consumption}")

    def do_exit(self, arg):
        'Exit the console'
        return True

if __name__ == '__main__':
    with app.app_context():
        Console().cmdloop()

