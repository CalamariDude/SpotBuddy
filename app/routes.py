from app import app
import json
from flask import request
import numpy as np

@app.route('/')
def main():
    print("wrong routes")
    return "wrong area"
frames = []
labels = []
@app.route('/data', methods=['GET', 'POST'])
def index(): 
    print("hello")   
    data = json.loads(request.data)
    print(data['label'])
    frames.append(data['frames'])
    labels.append(data['label'])
    # pose = request.form.get('frames')
    # label = request.form.get('label')
    # print('recieved pose', pose)
    # print('label recieved', label)
    return '0'

@app.route('/save', methods=['GET'])
def saver():
    np.save('frames', frames)
    np.save('labels', labels)
    return '0'