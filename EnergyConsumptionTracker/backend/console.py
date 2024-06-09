import cmd
from datetime import datetime
from backend.models.user import User
from backend.models.energy_record import EnergyRecord
from backend.models.analytics import Analytics
from backend.utils.db import db
from backend.app import create_app

app = create_app()

class EnergyConsumptionTrackerConsole(cmd.Cmd):
    intro = 'Welcome to the Energy Consumption Tracker console. Type help or ? to list commands.\n'
    prompt = '(ECT) '

    @staticmethod
    def _get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def _get_energy_record_by_id(record_id):
        return EnergyRecord.query.get(record_id)

    def do_create_user(self, arg):
        'Create a new user: create_user <username> <email> <password>'
        args = arg.split()
        if len(args) != 3:
            print("Invalid arguments. Usage: create_user <username> <email> <password>")
            return
        username, email, password = args
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        print(f"User {username} created with ID {user.id}")

    def do_get_user(self, arg):
        'Get user by ID: get_user <user_id>'
        try:
            user_id = int(arg)
        except ValueError:
            print("Invalid user ID. Usage: get_user <user_id>")
            return
        user = self._get_user_by_id(user_id)
        if user:
            print(f"User ID: {user.id}, Username: {user.username}, Email: {user.email}, Created at: {user.created_at}")
        else:
            print("User not found.")

    def do_create_energy_record(self, arg):
        'Create a new energy record: create_energy_record <user_id> <energy_consumed>'
        args = arg.split()
        if len(args) != 2:
            print("Invalid arguments. Usage: create_energy_record <user_id> <energy_consumed>")
            return
        try:
            user_id = int(args[0])
            energy_consumed = float(args[1])
        except ValueError:
            print("Invalid input. Usage: create_energy_record <user_id> <energy_consumed>")
            return
        user = self._get_user_by_id(user_id)
        if not user:
            print("User not found.")
            return
        record = EnergyRecord(user_id=user_id, energy_consumed=energy_consumed)
        db.session.add(record)
        db.session.commit()
        print(f"Energy record created with ID {record.id}")

    def do_get_energy_record(self, arg):
        'Get energy record by ID: get_energy_record <record_id>'
        try:
            record_id = int(arg)
        except ValueError:
            print("Invalid record ID. Usage: get_energy_record <record_id>")
            return
        record = self._get_energy_record_by_id(record_id)
        if record:
            print(f"Record ID: {record.id}, User ID: {record.user_id}, Energy Consumed: {record.energy_consumed}, Timestamp: {record.timestamp}")
        else:
            print("Energy record not found.")

    def do_exit(self, arg):
        'Exit the console'
        print('Goodbye!')
        return True

if __name__ == '__main__':
    with app.app_context():
        EnergyConsumptionTrackerConsole().cmdloop()

