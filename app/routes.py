from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    me = {
        "first_name": "KB",
        "last_name": "Osborne",
        "hobbies": "DIY stuff",
        "is_online": True
    }
    return me