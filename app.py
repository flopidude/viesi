
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import mysql

mydb = mysql.connector.connect(host="blincix.mysql.pythonanywhere-services.com", user="blincix", passwd="SoarinSet07", database="default")

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello_world():
    return 'Hello from Flask!'