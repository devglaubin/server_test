import requests

# Data to be sent in the POST request
url = "https://181.215.135.132:8000/"

print("pass0")
# Sending a POST request
response = requests.get(url)
print("pass1")

if response.status_code == 200:
    print("Success:", response.status_code)
else:
    print("Failed:", response.status_code)

print("Hello, World!")
