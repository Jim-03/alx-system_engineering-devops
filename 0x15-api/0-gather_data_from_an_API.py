#!/usr/bin/python3
"""
Module to return information from an api
Accepts an integer value as the employee's id
Uses the ID to fetch their todo progress.
"""
import requests
import sys


if __name__ == "__main__":
    """ Gets an employee's informstion given an id."""
    # The employee's id from the terminal
    employee_id = int(sys.argv[1])
    # send a get request
    r = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}"
            )
    # Capture the response in json format
    data = r.json()
    # Get the employee's name from the json string
    employee_name = data['name']
    # Find the employee's todo
    todo = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
            )
    # COnvert the todo to json
    todo_data = todo.json()
    # Find the tasks completed
    total = len(todo_data)
    completed_tasks = []
    for task in todo_data:
        if task['completed']:
            completed_tasks.append(task)
    print(f"Employee {employee_name} is done with tasks ", end='')
    print(f"({len(completed_tasks)}/{total}):")
    for task in todo_data:
        if task['completed']:
            print(f"\t {task['title']}")
