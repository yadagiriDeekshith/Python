import requests
resp=requests.get('http://127.0.0.1:8000/Api/')
print(resp.json())
