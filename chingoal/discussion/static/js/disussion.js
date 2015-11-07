
function populateList() {
    $.get("get_posts")
        .done(function(data) {
            var postDiv = $('');                                                //TODO -- id of division
            postDiv.html('');
            for (var i = 0; i < data.posts.length; i ++) {
                var post = data.posts[i];
                var post_html = $(post.html);
                postDiv.append(post_html);                                      //TODO -- get one post div and append replies to that
                for (var j = 0; j < post.replies.length; j ++) {
                    var reply = post.replies[j];
                    var reply_html = $(reply.html);
                    postDiv.append(reply_html);
                }
            }
        });
}


function new_reply_listener(e) {                                                //TODO -- add reply button
    
    var dt = new Date();
    var date_str = dt.toLocaleDateString();
    var time_str = dt.toLocaleTimeString('en-US', { hour12: false });
    var post_time = date_str + ' ' + time_str;

    var post_text = $()                                                         //TODO -- get post text from popup window

    $.post('post_reply')
        .done(function(data)) {
            var postDiv = $('');                                                //TODO -- get division of posts
            var post_html = $(data.post.html);
            postDiv.append(post_html);
    }
}


function new_post_listener(e) {
    
    var dt = new Date();
    var date_str = dt.toLocaleDateString();
    var time_str = dt.toLocaleTimeString('en-US', { hour12: false });
    var post_time = date_str + ' ' + time_str;

    var post_text = $()                                                         //TODO -- get post text from popup window

    $.post('post_post')
        .done(function(data)) {
            var postDiv = $('');                                                //TODO -- get division of posts
            var post_html = $(data.post.html);
            postDiv.append(post_html);
    }
}


$(document).ready(function() {
    populateList();

                                                                                //TODO -- add listener


    window.setInterval(populateList, 30000);

    function getCookie(name) {  
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });
});