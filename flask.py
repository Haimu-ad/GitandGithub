from threading import main_thread
from pip import main
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
    if _name_ -- "_main_":
        app.run(debug=True)