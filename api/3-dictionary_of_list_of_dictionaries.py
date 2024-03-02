import json
import requests
import sys

def get_all_users():
    """
    Fetches all users from the API.

    Returns:
    - dict: Dictionary containing user information.
    """
    # Replace the URL with the actual API endpoint for users
    api_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch user information")
        sys.exit(1)

def get_all_tasks():
    """
    Fetches tasks for all users from the API.

    Returns:
    - dict: Dictionary containing tasks for all users.
    """
    # Replace the URL with the actual API endpoint for tasks
    api_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch tasks for all users")
        sys.exit(1)

def export_to_json(users, tasks):
    """
    Exports all user tasks to a JSON file.

    Parameters:
    - users (dict): Dictionary containing user information.
    - tasks (dict): Dictionary containing tasks for all users.
    """
    filename = "todo_all_employees.json"
    data = {}

    for user in users:
        user_id = str(user["id"])
        username = user["username"]
        user_tasks = []

        for task in tasks:
            if task["userId"] == user["id"]:
                user_tasks.append({
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                })

        data[user_id] = user_tasks

    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=2)

    print(f"Data exported to {filename}")

if __name__ == "__main__":
    users = get_all_users()
    tasks = get_all_tasks()
    export_to_json(users, tasks)
