import requests
import getTerminalID as goget
import time
import os

url = "http://merlin.pythonanywhere.com"
my_id = goget.buildTID()

print(f"Listening for messages on ID: {my_id}")
print("Press Ctrl+C to stop\n")

last_message = None

try:
    while True:
        r = requests.get(f'{url}/listen', params={'trmnl-id': my_id})
        data = r.json()
        
        if data.get('status') == 200:
            msg = data.get('message')
            print(f"\n📩 New message: {msg}")
        elif data.get('status') == 404:
            pass
        
        time.sleep(2)
        
except KeyboardInterrupt:
    print("\nStopped listening.")