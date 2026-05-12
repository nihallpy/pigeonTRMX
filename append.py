# base append template


import requests
url = "http://merlin.pythonanywhere.com"

target = input("Enter target id: ")
message = None 
data = {
    'trmnl-id': target,
    'message': message
}

r = requests.post(f'{url}/append', json=data)
print(r.json())
