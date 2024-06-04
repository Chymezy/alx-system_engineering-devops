#!/usr/bin/python3
"""
This script fetches and displays the TODO list progress for a given employee ID
from a REST API.

Usage:
    ./0-gather_data_from_an_API.py <employee ID>
"""
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

            total_tasks = len(todos)
            completed_tasks = [task for task in todos if task['completed']]
            done_tasks = len(completed_tasks)
            print("Employee {} is done with tasks({}/{}):".format(
                user['name'], done_tasks, total_tasks)
            )
            for task in completed_tasks:
                print(f"\t {task['title']}")
