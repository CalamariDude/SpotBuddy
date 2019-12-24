from app import app
from flask import request
from pathlib import Path
import numpy as np
import json

frames = []
labels = []
if(Path('frames.npy').is_file()):
    frames_loaded = np.load('frames.npy', allow_pickle=True)
    labels_loaded = np.load('labels.npy', allow_pickle=True)
    for frame, label in zip(frames_loaded, labels_loaded):
        frames.append(frame)
        labels.append(label)


@app.route('/')
def main():
    print("wrong routes")
    return "wrong area"

@app.route('/data', methods=['GET', 'POST'])
def index(): 
    data = json.loads(request.data)
    global frames
    global labels
    frames.append(data['frames'])
    labels.append(data['label'])
    print(len(frames))
    return '0'

@app.route('/save', methods=['GET', 'POST'])
def saver():
    global frames
    global labels
    np.save('frames', frames)
    np.save('labels', labels)
    return '0'

@app.route('/delete', methods=['DELETE', 'POST'])
def delete():
    global frames
    global labels
    print("Current length of frames", len(frames))
    data = json.loads(request.data)
    index = data['index']
    print("deleting at index", index)
    return '0'

@app.route('/clear', methods=['GET', 'POST'])
def clear():
    global frames
    frames =[]
    global labels
    labels =[]
    return '0'
