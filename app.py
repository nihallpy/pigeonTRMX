### probably ignore this file its probably outdated

import os
import json
from flask import Flask, request
from flask import jsonify as jsonfy
# i hate whoever named it "jsonify" wtfff

app = Flask(__name__)

DATA_FILE = 'terminal_data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            data = json.load(f)
            return set(data.get('ids', [])), data.get('messages', {})
    return set(), {}

def save_data():
    with open(DATA_FILE, 'w') as f:
        json.dump({
            'ids': list(global_id),
            'messages': message_buffer
        }, f)

global_id, message_buffer = load_data()

@app.route('/database/', methods=['GET', 'POST'])
def database():
  if request.method == 'POST':
    data = request.get_json()
    terminal_id = data.get('trmnl-id')
    
    if terminal_id not in global_id:
      global_id.add(terminal_id)
      save_data()  
      return jsonfy({'status': 201, 'msg': 'good job skid'}), 201
    else:
      return jsonfy({'status': 409, 'err': 'already-exist'}), 409
  
  elif request.method == 'GET':
    terminal_id = request.args.get('trmnl-id')
    if terminal_id in global_id:
      return jsonfy({'status': 200, 'msg': 'good job skid'}), 200
    else:
      return jsonfy({'status': 404, 'msg': 'not-exist', 'advice': 'try running starter.py if it says id already exists even tho u got this error its bugged idk'})

@app.route('/append/', methods=['POST'])
def append():
    data = request.get_json()
    target_id = data.get('trmnl-id')
    msg = data.get('message')
    
    print(f"DEBUG append - target_id: {target_id}")
    print(f"DEBUG append - global_id before check: {global_id}")
    print(f"DEBUG append - is target in global_id? {target_id in global_id}")
    
    if target_id in global_id:
        message_buffer[target_id] = msg
        save_data()  
        print(f"DEBUG append - message_buffer now: {message_buffer}")
        return jsonfy({'status': 201, 'msg': 'good job skid'}), 201
    else:
        return jsonfy({'status': 404, 'msg': 'not-exist'}), 404
        
      
@app.route('/listen/', methods=['GET'])
def listen():
    self_id = request.args.get('trmnl-id')
    if self_id in message_buffer:
      return jsonfy({'status': 200, 'message': message_buffer[self_id]}), 200
    else:
      return jsonfy({'status': 404, 'err': 'not-exist'}), 404
      
@app.route('/debugging/', methods=['GET'])
def debugging():
  return jsonfy({'global_id': list(global_id), 'message_buffer': message_buffer})  

if __name__ == "__main__":
  app.run(debug=False)
