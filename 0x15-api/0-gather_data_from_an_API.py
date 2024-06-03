#!/usr/bin/python3
""" module to return information from an api."""
import sys
import requests


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    r = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}"
            )
    data = r.json()
    employee_name = data['name']
    todo = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
            )
    todo_data = todo.json()
    completed_tasks = 0
    for task in todo_data:
        if task['completed']:
            completed_tasks += 1
    print(f"Employee {employee_name} is done with tasks
          ({completed_tasks}/{len(todo_data)}): ")
    for task in todo_data:
        if task['completed']:
            print(f"\t {task['title']}")
