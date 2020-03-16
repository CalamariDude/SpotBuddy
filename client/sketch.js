// Copyright (c) 2019 ml5
//
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

/* ===
ml5 Example
PoseNet example using p5.js
=== */

let video;
let poseNet;
let poses = [];

//Save the current models 
function saveData() {
fetch('http://localhost:5000/save',{
  method:'POST',
  body:JSON.stringify({}),
  headers: {'Content-Type': 'text/plain'}
}).then(function(){
console.log("saved")
}).catch(function(){
console.log("failed to save")
});
}

function clearData() {
fetch('http://localhost:5000/clear', {
  method:'POST',
  body:{},
  headers: {'Content-Type': 'text/plain'}
}).then(function(){
console.log("successfull clear")
}).catch(function(){
console.log("failed to clear")
});
}

function setup() {
createCanvas(640, 480);
video = createCapture(VIDEO);
video.size(width, height);
// Create a new poseNet method with a single detection
poseNet = ml5.poseNet(video, modelReady);
// This sets up an event that fills the global variable "poses"
// with an array every time new poses are detected
poseNet.on('pose', function(results) {
poses = results;
});
// Hide the video element, and just show the canvas
video.hide();
}

//Hook to delete a specific training point
function deleteData() {
var index = document.getElementById('index').value;
fetch('http://localhost:5000/delete', {
method:'POST',
data: {index:index},
headers: {'Content-Type': 'text/plain'}
}).then(function(){
console.log("Success")
}).catch(function(){
console.log("failure")
})
}

//Hook to change status text when model loaded
function modelReady() {
select('#status').html('Model Loaded');
}

var capture = [];
let counter = 0
var date = 0
var startcapturing = false
//Hook for capturing the good label data
function startcapturinggood() {
startcapturing = true
label = 0
}
//Hook for capturing the bad label data
function startcapturingbad(){
startcapturing = true
label = 1
}

//Draws the points on the figure
function draw() {  
image(video, 0, 0, width, height);
console.log(startcapturing)
//Keep updating the timer
if(startcapturing == false){
capture = []
date = Date.now()
var elapsed = 0

}
//If there is hook to start capturing, start calculating the elapsed time
if (startcapturing == true){
elapsed = Date.now()
capture.push(poses)
let seconds = 4
console.log(elapsed + " " + date)
//if time is elapsed, send the data and label to the server
if(elapsed > date + (seconds * 1000)){
  console.log("capture", capture)
  startcapturing = false
  var data ={
    frames: capture,
    label: label
  };
  //POST request to add a training data
  const response = fetch('http://localhost:5000/data', 
  {
    method: 'POST', 
    body: JSON.stringify(data), 
    headers: {'Content-Type': 'text/plain'}
  }
  ).then(function(df){
    console.log(df)
    console.log('Success:', JSON.stringify(json))
    var json =  response.json();
  })
  .catch(function(){
    console.log('fail')
  })
  }
}
// We can call both functions to draw all keypoints and the skeletons
drawKeypoints();
drawSkeleton();
}

// A function to draw ellipses over the detected keypoints
function drawKeypoints()  {
// Loop through all the poses detected
for (let i = 0; i < poses.length; i++) {
// For each pose detected, loop through all the keypoints
let pose = poses[i].pose;
for (let j = 0; j < pose.keypoints.length; j++) {
  // A keypoint is an object describing a body part (like rightArm or leftShoulder)
  let keypoint = pose.keypoints[j];
  // Only draw an ellipse is the pose probability is bigger than 0.2
  if (keypoint.score > 0.2) {
    fill(255, 0, 0);
    noStroke();
    ellipse(keypoint.position.x, keypoint.position.y, 10, 10);
  }
}
}
}

// A function to draw the skeletons
function drawSkeleton() {
// Loop through all the skeletons detected
for (let i = 0; i < poses.length; i++) {
let skeleton = poses[i].skeleton;
// For every skeleton, loop through all body connections
for (let j = 0; j < skeleton.length; j++) {
  let partA = skeleton[j][0];
  let partB = skeleton[j][1];
  stroke(255, 0, 0);
  line(partA.position.x, partA.position.y, partB.position.x, partB.position.y);
}
}
}