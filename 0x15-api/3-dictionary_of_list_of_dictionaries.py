#!/usr/bin/python3
"""
This script fetches all task data for every employee from a REST API and
exports the data to a JSON file, structured by user ID.

Usage:
    ./3-dictionary_of_list_of_dictionaries.py
"""
import json
import requests

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    if users_response.ok and todos_response.ok:
        users = users_response.json()
        todos = todos_response.json()

        user_tasks = {}
        for user in users:
            user_id = str(user['id'])
            user_tasks[user_id] = [
                {
                    "username": user['username'],
                    "task": todo['title'],
                    "completed": todo['completed']
                }
                for todo in todos if todo['userId'] == user['id']
            ]

        with open("todo_all_employees.json", 'w') as jsonfile:
            json.dump(user_tasks, jsonfile)
