import requests
response = requests.get("http://www.google.com")
a = len(response.text)
print(a)