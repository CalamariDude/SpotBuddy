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
    del frames[index]
    del labels[index]
    return '0'

@app.route('/clear', methods=['GET', 'POST'])
def clear():
    global frames
    frames =np.asarray([])
    global labels
    labels =np.asarray([])
    return '0'
