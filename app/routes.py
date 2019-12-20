from app import app
from flask import request
from pathlib import Path
import numpy as np
import json

frames = []
labels = []
if(Path('frames.npy').is_file()):
    frames = np.load('frames.npy')
    labels = np.load('labels.npy')

@app.route('/')
def main():
    print("wrong routes")
    return "wrong area"

@app.route('/data', methods=['GET', 'POST'])
def index(): 
    data = json.loads(request.data)
    print(data['label'])
    frames.append(data['frames'])
    labels.append(data['label'])
    return '0'

@app.route('/save', methods=['GET'])
def saver():
    np.save('frames', frames)
    np.save('labels', labels)
    return '0'