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

  vid = createVideo(
    ['http://mirrors.standaloneinstaller.com/video-sample/small.mp4'],
    vidLoad
  );

  vid.size(100, 100);
}

// This function is called when the video loads
function vidLoad() {
  vid.loop();
  vid.volume(0);
}
