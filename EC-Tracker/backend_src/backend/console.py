from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, EnergyRecord, Analytics

app = create_app()
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'EnergyRecord': EnergyRecord, 'Analytics': Analytics}

def create_user(username, email, password):
    try:
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        print(f"User {username} created successfully with ID {user.id}.")
    except Exception as e:
        print(f"Error creating user: {e}")

def update_user(user_id, **kwargs):
    user = User.query.get(user_id)
    if not user:
        print(f"User ID {user_id} not found.")
        return
    try:
        for key, value in kwargs.items():
            setattr(user, key, value)
        db.session.commit()
        print(f"User ID {user_id} updated successfully.")
    except Exception as e:
        print(f"Error updating user: {e}")

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        print(f"User ID {user_id} not found.")
        return
    try:
        db.session.delete(user)
        db.session.commit()
        print(f"User ID {user_id} deleted successfully.")
    except Exception as e:
        print(f"Error deleting user: {e}")

def create_energy_record(user_id, date, consumption):
    user = User.query.get(user_id)
    if not user:
        print(f"User ID {user_id} not found.")
        return
    try:
        record = EnergyRecord(user_id=user.id, date=date, consumption=consumption)
        db.session.add(record)
        db.session.commit()
        print(f"Energy record for User ID {user_id} on {date} created successfully with Record ID {record.id}.")
    except Exception as e:
        print(f"Error creating energy record: {e}")

def update_energy_record(record_id, **kwargs):
    record = EnergyRecord.query.get(record_id)
    if not record:
        print(f"Energy record ID {record_id} not found.")
        return
    try:
        for key, value in kwargs.items():
            setattr(record, key, value)
        db.session.commit()
        print(f"Energy record ID {record_id} updated successfully.")
    except Exception as e:
        print(f"Error updating energy record: {e}")

def delete_energy_record(record_id):
    record = EnergyRecord.query.get(record_id)
    if not record:
        print(f"Energy record ID {record_id} not found.")
        return
    try:
        db.session.delete(record)
        db.session.commit()
        print(f"Energy record ID {record_id} deleted successfully.")
    except Exception as e:
        print(f"Error deleting energy record: {e}")

def inspect_user(user_id):
    user = User.query.get(user_id)
    if not user:
        print(f"User ID {user_id} not found.")
        return
    print(f"User ID: {user.id}")
    print(f"Username: {user.username}")
    print(f"Email: {user.email}")
    print(f"Created At: {user.created_at}")
    print(f"Updated At: {user.updated_at}")

def interpret_command(command):
    try:
        parts = command.split()
        action = parts[0].lower()
        if action == 'create':
            if parts[1].lower() == 'user':
                _, _, username, email, password = parts
                create_user(username, email, password)
            elif parts[1].lower() == 'energyrecord':
                _, _, user_id, date, consumption = parts
                create_energy_record(int(user_id), date, float(consumption))
        elif action == 'update':
            if parts[1].lower() == 'user':
                _, _, user_id, *updates = parts
                update_fields = dict(zip(updates[::2], updates[1::2]))
                update_user(int(user_id), **update_fields)
            elif parts[1].lower() == 'energyrecord':
                _, _, record_id, *updates = parts
                update_fields = dict(zip(updates[::2], updates[1::2]))
                update_energy_record(int(record_id), **update_fields)
        elif action == 'delete':
            if parts[1].lower() == 'user':
                _, _, user_id = parts
                delete_user(int(user_id))
            elif parts[1].lower() == 'energyrecord':
                _, _, record_id = parts
                delete_energy_record(int(record_id))
        elif action == 'inspect':
            if parts[1].lower() == 'user':
                _, _, user_id = parts
                inspect_user(int(user_id))
        else:
            print("Unknown command.")
    except Exception as e:
        print(f"Error processing command: {e}")
        print("Use the following command formats:")
        print("Create User: create user <username> <email> <password>")
        print("Update User: update user <user_id> <field> <new_value> [<field> <new_value>...]")
        print("Delete User: delete user <user_id>")
        print("Create Energy Record: create energyrecord <user_id> <date> <consumption>")
        print("Update Energy Record: update energyrecord <record_id> <field> <new_value> [<field> <new_value>...]")
        print("Delete Energy Record: delete energyrecord <record_id>")
        print("Inspect User: inspect user <user_id>")

def main():
    print("Welcome to the Energy Consumption Tracker Console")
    print("Type 'help' for a list of commands.")
    print("Type 'exit' or 'quit' to exit the console.")
    while True:
        command = input("Command> ")
        if command.lower() in ['exit', 'quit']:
            break
        elif command.lower() == 'help':
            print("Available commands:")
            print("Create User: create user <username> <email> <password>")
            print("Update User: update user <user_id> <field> <new_value> [<field> <new_value>...]")
            print("Delete User: delete user <user_id>")
            print("Create Energy Record: create energyrecord <user_id> <date> <consumption>")
            print("Update Energy Record: update energyrecord <record_id> <field> <new_value> [<field> <new_value>...]")
            print("Delete Energy Record: delete energyrecord <record_id>")
            print("Inspect User: inspect user <user_id>")

if __name__ == '__main__':
    main()

