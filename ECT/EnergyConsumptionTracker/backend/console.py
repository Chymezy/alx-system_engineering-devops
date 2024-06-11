import os
from flask import Flask
from flask.cli import with_appcontext
from backend.utils.db import db
from backend.models.user import User
from backend.models.energy_record import EnergyRecord
from backend.models.analytics import Analytics
import click

# Importance: Facilitates database management and testing via a user-friendly CLI.

app = Flask(__name__)
app.config.from_object('backend.config.Config')
db.init_app(app)

@click.command(name='create_user')
@click.argument('username')
@click.argument('password')
@with_appcontext
def create_user(username, password):
    # Function to create a user

@click.command(name='create_energy_record')
@click.argument('user_id')
@click.argument('consumption')
@with_appcontext
def create_energy_record(user_id, consumption):
    # Function to create an energy record

@click.command(name='view_energy_records')
@with_appcontext
def view_energy_records():
    # Function to view all energy records

@click.command(name='update_energy_record')
@click.argument('record_id')
@click.argument('consumption')
@with_appcontext
def update_energy_record(record_id, consumption):
    # Function to update an energy record

@click.command(name='delete_energy_record')
@click.argument('record_id')
@with_appcontext
def delete_energy_record(record_id):
    # Function to delete an energy record

app.cli.add_command(create_user)
app.cli.add_command(create_energy_record)
app.cli.add_command(view_energy_records)
app.cli.add_command(update_energy_record)
app.cli.add_command(delete_energy_record)

if __name__ == "__main__":
    app.run()

