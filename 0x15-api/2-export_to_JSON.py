#!/usr/bin/python3
"""
This script fetches task data for a given employee ID from a REST API and
exports the data to a JSON file.

Usage:
    ./2-export_to_JSON.py <employee ID>
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        user_id = argv[1]
        user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        todos_url = (
                f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
                )

        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        if user_response.ok and todos_response.ok:
            user = user_response.json()
            todos = todos_response.json()

            tasks = []
            for task in todos:
                task_dict = {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": user["username"]
                }
                tasks.append(task_dict)

            tasks_dict = {user_id: tasks}

            with open(f"{user_id}.json", 'w') as jsonfile:
                json.dump(tasks_dict, jsonfile)
