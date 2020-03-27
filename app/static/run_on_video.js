let video;
let poseNet;
let poses = [];

var capture = [];
let counter = 0
var date = 0
var startcapturing = false
let vid;

function setup() {
  noCanvas();

  // you need to have the python server running from data folder goodserver.py
  // in order to access videos through JS - shatz
  vid = createVideo(
    ['http://0.0.0.0:8003/shatz.mp4'],
    // vidLoad // this is a function
    // vidload()
  );
  // vid.hide()
  vid.size(100, 100);
}

// This function is called when the video loads
function vidLoad() {
  vid.loop();
  vid.volume(0);
}


function pass_vid_to_flask() {
    for (let step = 0; step < 1000; step++) {
      // Runs 5 times, with values of step 0 through 4.
      vid.play()
      vid.stop()
      console.log('Walking east one step');
    }

    console.log('almost dere')
}
