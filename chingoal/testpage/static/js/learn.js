
var userLevel;
var userLesson;
var currLevel;    
var currLesson;

function setProgressBar() {
    $('.progress-bar').css('width', '0%');
    $('#progress-text').html('0% Complete');
}

function updateProgressBar() {
    var currChapter = $('#hidden_curr_chapter').html();

    var perc = currChapter / 5 * 100;
    console.log('perc is ' + perc );
    $('.progress-bar').css('width', perc + '%');
    $('#progress-text').html(perc + '% Complete');
}

function validateButtons(currLevel, currLesson, userLevel, userLesson) {        
    if (userLevel <= currLevel) {
        if (userLesson <= currLesson) {
            $('#skipBtn').prop('disabled', true);
        }
    }
    // TODO enable button??
}

function generateLearn(currLevel, currLesson, currChapter) {
    $.get('/testpage/get-learn-json/' + currLevel + '/' + currLesson + '/' + currChapter)
        .done(function(data){
            $('.panel-body').html('');
            var learningBody = $(data.html);
            $('.panel-body').append(learningBody);

            $('#hidden_username').html(data.current_username);
            $('#hidden_user_level').html(data.current_userLevel);
            $('#hidden_user_lesson').html(data.current_userLesson);

            if (data.learn_type == 'text') {
                // do nothing                
            } else {
                $.holdReady(true);
                $.getScript('/static/js/visualizeWave.js', function() {});
                $.getScript('/static/js/custom_audio_revised.js', function() {});
                $.getScript('/static/js/learn_audio.js', function() {
                    console.log($('#checkBtn'));
                    $('#checkBtn').html('Take Test!');
                    $('#checkBtn').unbind('click');
                    $('#checkBtn').on('click', function(e){
                        e.preventDefault();                    
                        if (userLevel <= currLevel) {
                            window.location.replace('/testpage/get-test/' + currLevel);
                        } else {
                            window.location.replace('/testpage');
                        }
                    });                                        
                    $.holdReady(false);
                    $('#learn_name').html($('#hidden_text').html());
                    console.log('In learn js username is ' + $('#hidden_username').html());
                });
            }
        });
    
}

function checkClicked() {
    var answer = $('#hidden_answer').html();
    $('#answer-modal').html(answer);
    var userAnswer = $('input[name=optionsRadiosInline]:checked').attr('value');
    if(!userAnswer) {
        $('#checkBtn').addClass('no-modal');
        alert("Please choose from one of the following three...");
    } else {
        if ($('#checkBtn').hasClass('no-modal')) {
            $('#checkBtn').removeClass('no-modal');
        }
        if (answer == userAnswer) {
            $('.modal-body').css('background-color', '#d6e9c6');
        } else {
            $('.modal-body').css('background-color', '#ebccd1');
        }
    }
}

function nextClicked(currLevel, currLesson) {
    var currChapter = $('#hidden_curr_chapter').html();
    if (currChapter < 5) {
        generateLearn(currLevel, currLesson, ++currChapter);
        $('#hidden_curr_chapter').html(currChapter);
    // } else if (currChapter == 4) {
        // window.location.replace('/testpage/get-learn-audio/' + currLevel + '/' + currLesson);
    } else {        
        $.post('/testpage/write-history', {'currLevel':currLevel, 'currLesson':currLesson}).done();
        if (userLevel < currLevel) {
            //!!!!
            // $.get('/testpage').done();
        } else {
            //!!!!
            // $.get('/testpage/get-test/' + currLevel).done();
        }
        

    }    
    
}


function getParam() {
    userLevel = $('#hidden_user_level').html();
    userLesson = $('#hidden_user_lesson').html();
    currLevel = $('#hidden_curr_level').html();    
    currLesson = $('#hidden_curr_lesson').html();
}

$(document).ready(function(){
    getParam();    

    setProgressBar();    
    validateButtons(currLevel, currLesson, userLevel, userLesson);
    generateLearn(currLevel, currLesson, 1);

    $('#checkBtn').on('click', checkClicked);

    $('.modal-dialog').on('click', '#nextBtn', function (e) {
        // e.stopPropagation();
        updateProgressBar();
        $('.modal').modal('toggle');
        nextClicked(currLevel, currLesson);
    });


    $('#myModal').on('show.bs.modal', function (e) {
        var button = e.relatedTarget;

        if($(button).hasClass('no-modal')) {
            e.preventDefault();
        }  
    });

});