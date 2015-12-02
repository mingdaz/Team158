
// user file format
// userupload_{% current_level %}_{% current_lesson %}_{% current_chapter %}_{% user attempt %}


var audioContext = null;
var context = null;

var audio = null;
var userAudio = null;


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

function playUserAudioClicked() {
    // TODO change file name and url for matching user level and lesson



    if (userAudio.paused) {
        userAudio.play();
        $('#playUserAudioButton').removeClass('fa-play');
        $('#playUserAudioButton').addClass('fa-pause');        
    } else {
        userAudio.pause();
        $('#playUserAudioButton').removeClass('fa-pause');
        $('#playUserAudioButton').addClass('fa-play');
    }
}

function drawLearnAudio(audioUrl) {
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

}


$(document).ready(function () {

    // TODO change src url

    var audioUrl = "https://s3.amazonaws.com/chingoal/audio/test.mp3";    

    audio = new Audio();
    audio.src = audioUrl;

    drawLearnAudio(audioUrl);

    $('#playButton').on('click', playButtonClicked);
    
    $(audio).on('ended', function() {
        $('#playButton').removeClass('fa-pause');
        $('#playButton').addClass('fa-play');
    });

    // TODO change src url

    var userAudioUrl = "https://s3.amazonaws.com/chingoal/audio/userupload.wav";
    
    userAudio = new Audio();
    userAudio.src = userAudioUrl;

    

    $('#playUserAudioButton').on('click', playUserAudioClicked);

    $(userAudio).on('ended', function() {
        $('#playUserAudioButton').removeClass('fa-pause');
        $('#playUserAudioButton').addClass('fa-play');
    })

})