from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "This is a simple Web app developed in python by Aditya. I have used Flask to deploy it as a web app."