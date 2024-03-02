import json
import requests
import sys

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

def export_to_json(tasks):
    """
    Exports all user tasks to a JSON file.

    Parameters:
    - tasks (dict): Dictionary containing tasks for all users.
    """
    filename = "todo_all_employees.json"
    data = {}

    for task in tasks:
        user_id = str(task["userId"])
        if user_id not in data:
            data[user_id] = []
        
        data[user_id].append({
            "username": task["username"],
            "task": task["title"],
            "completed": task["completed"]
        })

    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=2)

    print(f"Data exported to {filename}")

if __name__ == "__main__":
    tasks = get_all_tasks()
    export_to_json(tasks)
