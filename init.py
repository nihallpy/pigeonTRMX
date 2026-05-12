import getTerminalID as goget
import requests


url = "http://merlin.pythonanywhere.com"

TUID = goget.buildTID()
data = {'trmnl-id': TUID}
p = requests.post(f'{url}/database', json=data)
print(p.json())

print("running check if it returns 409 or 200 youre good")
r = requests.get(f'{url}/database', params=data)
print(r.json())
