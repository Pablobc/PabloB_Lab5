# app.py
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="pdfhacker",
  password="ITKBWiCFedvha3nv9wzx"
)

print(mydb)