import sys
import json
import requests

def get_user_tasks(user_id):
    # Fetching user data
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    user_data = user_response.json()

    # Fetching user's tasks
    tasks_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
    tasks_data = tasks_response.json()

    return user_data, tasks_data

def export_to_json(user_id, tasks):
    data_to_export = {str(user_id): [{"task": task["title"], "completed": task["completed"], "username": user_data["username"]} for task in tasks]}
    filename = f'{user_id}.json'

    with open(filename, 'w') as json_file:
        json.dump(data_to_export, json_file, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    try:
        user_data, tasks_data = get_user_tasks(user_id)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

    export_to_json(user_id, tasks_data)
    print(f"Data exported to {user_id}.json successfully.")
