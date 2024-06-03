#!/usr/bin/python3
import sys
import requests
""" Module to return information from an api"""


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
    completed_tasks = 0
    for task in todo_data:
        if task['completed']:
            completed_tasks += 1
    print(f"Employee {employee_name} is done with tasks
          ({completed_tasks}/{len(todo_data)}): ")
    for task in todo_data:
        if task['completed']:
            print(f"\t {task['title']}")
