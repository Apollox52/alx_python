import sys
import json
import requests

def get_user_tasks(user_id):
    """
    Fetch user information and tasks based on the provided user ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        tuple: A tuple containing user data (dict) and tasks data (list of dicts).
    """
    # Fetching user data
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    user_data = user_response.json()

    # Fetching user's tasks
    tasks_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
    tasks_data = tasks_response.json()

    return user_data, tasks_data

def export_to_json(user_id, tasks):
    """
    Export user tasks to a JSON file.

    Args:
        user_id (int): The ID of the user.
        tasks (list): List of tasks for the user.

    Returns:
        None
    """
    # Creating a dictionary in the specified format
    data_to_export = {str(user_id): [{"task": task["title"], "completed": task["completed"], "username": user_data["username"]} for task in tasks]}
    filename = f'{user_id}.json'

    # Writing the data to a JSON file
    with open(filename, 'w') as json_file:
        json.dump(data_to_export, json_file, indent=2)

if __name__ == "__m
