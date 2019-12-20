from app import app
from flask import request
from pathlib import Path
import numpy as np
import json

frames = np.asarray([])
labels = np.asarray([])
if(Path('frames.npy').is_file()):
    frames = np.load('frames.npy', allow_pickle=True)
    labels = np.load('labels.npy', allow_pickle=True)

@app.route('/')
def main():
    print("wrong routes")
    return "wrong area"

@app.route('/data', methods=['GET', 'POST'])
def index(): 
    data = json.loads(request.data)
    print(data['label'])
    global frames
    global labels
    frames = np.append(frames, data['frames'])
    labels = np.append(labels, data['label'])
    print("frames shape ", frames.shape)
    print("labels shape ", labels.shape)
    return '0'

@app.route('/save', methods=['GET'])
def saver():
    global frames
    global labels
    np.save('frames', frames)
    np.save('labels', labels)
    return '0'

@app.route('/delete', methods=['DELETE'])
def delete():
    global frames
    global labels
    data = json.loads(request.data)
    index = data['index']
    del frames[index]
    del labels[index]
    return '0'

@app.route('/clear', methods=['GET'])
def clear():
    global frames
    frames =np.asarray([])
    global labels
    labels =np.asarray([])
    return '0'
