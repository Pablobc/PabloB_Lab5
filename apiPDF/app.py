# app.py
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="pdfhacker",
  password="ITKBWiCFedvha3nv9wzx",
  database="pdfdatos"
)
mycursor = mydb.cursor()

print(mydb)

@app.route("/grida")

def get_data():
    mycursor.execute("SELECT * FROM datos")
    myresult = mycursor.fetchall()
    payload = []
    content = {}
    for result in myresult:
        content = {'id':result[4],'contrasenia': result[0], 'dip': result[1], 'so': result[2], 'version': result[3]}
        payload.append(content)
        content = {}
    print(payload)
    return jsonify(payload)

