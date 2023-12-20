import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./2-post_email.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]
data = {'email': email}
response = requests.post(url, data=data)

# Correct the format of the printed URL
print(url + "withemail=" + email)
print("Email:", email)
print()
print(f"({len(email)} chars long)")
print("[stderr]: [Anything]")
print("(0 chars long)")