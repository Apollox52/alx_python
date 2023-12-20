import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./2-post_email.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]
data = {'email': email}
response = requests.post(url, data=data)

print("Your email is:", email)
print(response.text)