import requests
import sys

def get_employee_info(employee_id):
    # Get employee details
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    # Get employee's TODO list
    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Extract relevant information
    employee_name = employee_data['name']
    total_tasks = len(todo_data)
    completed_tasks = sum(task['completed'] for task in todo_data)
    completed_task_titles = [task['title'] for task in todo_data if task['completed']]

    # Display the information on standard output
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for task_title in completed_task_titles:
        print(f"\t{task_title}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
