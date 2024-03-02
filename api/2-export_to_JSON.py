import json
import requests
import sys
"""
    Fetches tasks for a specified user from the API.

    Parameters:
    - user_id (int): The ID of the user.

    Returns:
    - list: List of tasks for the specified user.
    """
def get_user_tasks(user_id):
    """
    Fetches tasks for a specified user from the API.

    Parameters:
    - user_id (int): The ID of the user.

    Returns:
    - list: List of tasks for the specified user.
    """
    # Replace the URL with the actual API endpoint for tasks
    api_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch tasks for user {user_id}")
        sys.exit(1)

def export_to_json(user_id, tasks):
    """
    Exports user tasks to a JSON file.

    Parameters:
    - user_id (int): The ID of the user.
    - tasks (list): List of tasks for the specified user.
    """
    filename = f"{user_id}.json"
    data = {str(user_id): [{"task": task["title"], "completed": task["completed"], "username": task["username"]} for task in tasks]}

    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=2)

    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python export_to_json.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    tasks = get_user_tasks(user_id)
    export_to_json(user_id, tasks)
