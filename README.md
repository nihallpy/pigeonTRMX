```
# 🐦 PigeonTRMX

A lightweight terminal-based messaging system built with Flask. Register your terminal, send messages, and listen for incoming messages — all through simple HTTP requests.

## 📋 How It Works

1. **Register** – Each terminal gets a unique ID based on its architecture (CPU + OS).
2. **Send** – A terminal pushes a message to another terminal's ID using `/append/`.
3. **Listen** – The target terminal continuously polls `/listen/` and displays new messages.

---

## 🚀 Setup

### Prerequisites
- Python 3.7+
- pip

### Install Dependencies
```bash
pip install requests
```

Clone the Repository

```bash
git clone https://github.com/nihallpy/pigeonTRMX.git
cd pigeonTRMX
```

---

📡 Usage

The server is already hosted at http://merlin.pythonanywhere.com. Just run the client scripts:

1. Register Your Terminal

```bash
python init.py
```

This registers your terminal's unique ID with the server.

2. Listen for Messages

```bash
python listen.py
```

Polls the server every 2 seconds and prints new messages addressed to you.

3. Send a Message

```bash
python append.py
```

Enter the target terminal ID and your message.

---

🔌 API Endpoints (for reference)

Method Endpoint Description
POST /database/ Register a new terminal ID. Body: {"trmnl-id": "..."}
GET /database/ Check if an ID exists. Query: ?trmnl-id=...
POST /append/ Store a message for a target ID. Body: {"trmnl-id": "...", "message": "..."}
GET /listen/ Get queued message for your ID. Query: ?trmnl-id=...
GET /debugging/ View all registered IDs and messages (debug only)

---

📝 Notes

· Each terminal ID is a unique MD5 hash of your device's architecture.
· Messages are stored until the recipient listens.
· The server clears messages after they're delivered (read-once).

---

🛠️ Self-Hosting (Optional)

If you want to run your own server:

```bash
pip install flask
python app.py
```

Then update the url variable in listen.py and append.py to your server's address.