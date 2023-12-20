import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./6-my_github.py <username> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
personal_access_token = sys.argv[2]
url = "https://api.github.com/user"


auth = (username, personal_access_token)

response = requests.get(url, auth=auth)

if response.status_code == 200:
    user_data = response.json()
    print(user_data.get('id'))
else:
    print(None)