from app import app
import json
from flask import request

@app.route('/')
def main():
    print("wrong routes")
    return "wrong area"

@app.route('/data', methods=['GET', 'POST'])
def index(): 
    print("hello")   
    data = request.json
    print(data)
    # pose = request.form.get('frames')
    # label = request.form.get('label')
    # print('recieved pose', pose)
    # print('label recieved', label)
    return '0'