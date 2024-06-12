import cmd
from datetime import datetime
from backend.app import create_app
from backend.utils.db import db
from backend.models.user import User
from backend.models.energy_record import EnergyRecord
from backend.models.analytics import Analytics

app = create_app()
app.app_context().push()

class EnergyConsole(cmd.Cmd):
    intro = 'Welcome to the Energy Management Console. Type help or ? to list commands.\n'
    prompt = '(energy_mgmt) '

    def do_create_user(self, arg):
        'Create a new user: create_user <username> <email> <password>'
        args = arg.split()
        if len(args) != 3:
            print("Usage: create_user <username> <email> <password>")
            return
        username, email, password = args
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        print(f"User {username} created.")

    def do_update_user(self, arg):
        'Update user email: update_user <user_id> <new_email>'
        args = arg.split()
        if len(args) != 2:
            print("Usage: update_user <user_id> <new_email>")
            return
        user_id, new_email = args
        user = User.query.get(user_id)
        if user:
            user.email = new_email
            user.updated_at = datetime.utcnow()
            db.session.commit()
            print(f"User {user.username} updated.")
        else:
            print("User not found.")

    def do_delete_user(self, arg):
        'Delete a user: delete_user <user_id>'
        user = User.query.get(arg)
        if user:
            db.session.delete(user)
            db.session.commit()
            print(f"User {user.username} deleted.")
        else:
            print("User not found.")

    def do_list_users(self, arg):
        'List all users'
        users = User.query.all()
        for user in users:
            print(f"{user.id}: {user.username} ({user.email})")

    def do_create_energy_record(self, arg):
        'Create a new energy record: create_energy_record <user_id> <energy_consumed>'
        args = arg.split()
        if len(args) != 2:
            print("Usage: create_energy_record <user_id> <energy_consumed>")
            return
        user_id, energy_consumed = args
        record = EnergyRecord(user_id=user_id, energy_consumed=energy_consumed)
        db.session.add(record)
        db.session.commit()
        print(f"Energy record for user {user_id} created.")

    def do_list_energy_records(self, arg):
        'List all energy records for a user: list_energy_records <user_id>'
        records = EnergyRecord.query.filter_by(user_id=arg).all()
        for record in records:
            print(f"{record.id}: {record.energy_consumed} at {record.timestamp}")

    def do_exit(self, arg):
        'Exit the console'
        return True

if __name__ == '__main__':
    EnergyConsole().cmdloop()

