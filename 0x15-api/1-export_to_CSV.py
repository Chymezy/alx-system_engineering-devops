#!/usr/bin/python3
"""
This script fetches task data for a given employee ID from a REST API and
exports the data to a CSV file.

Usage:
    ./1-export_to_CSV.py <employee ID>
"""
import csv
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

            with open(f"{user_id}.csv", 'w', newline='') as csvfile:
                taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

                for task in todos:
                    taskwriter.writerow([
                        user_id,
                        user['username'],
                        task['completed'],
                        task['title']
                    ])
