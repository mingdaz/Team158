
var audioContext = null;
var context = null;

var audio = null;



function playButtonClicked() {    
    if (audio.paused) {
        audio.play();
        $('#playButton').removeClass('fa-play');
        $('#playButton').addClass('fa-pause');
    } else {
        audio.pause();
        $('#playButton').removeClass('fa-pause');
        $('#playButton').addClass('fa-play');
    }

}

function playUserButtonClicked() {

}

function getBuffer() {

}


$(document).ready(function () {

    // TODO change src url
    var audioUrl = "https://s3.amazonaws.com/chingoal/audio/test.mp3";
    

    audio = new Audio();
    audio.src = audioUrl;

    $('#playButton').on('click', playButtonClicked);

    audioContext = window.AudioContext || window.webkitAudioContext;
    context = new audioContext();

    var xmlReq = new XMLHttpRequest();
    var learnBuffers = [];
    xmlReq.open("GET", audioUrl, true);
    xmlReq.responseType = "arraybuffer";
    xmlReq.onreadystatechange = function() {        
        context.decodeAudioData(xmlReq.response, function (buffer) {
            drawBuffer(
                $('#wave_learn').get(0).width, 
                $('#wave_learn').get(0).height, 
                $('#wave_learn').get(0).getContext('2d'), 
                buffer.getChannelData(0));
        });
    };
    xmlReq.send();

})