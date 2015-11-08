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

function getMultipleChoicw() {
    var list = $("#question"); 
    var max_entry = list.data("max-entry")
   
    $.get("/testpage/test-add-q-mc/"+max_entry)
      .done(function(data) {
              item = data.html;
              var new_item = $(item);
              new_item.data("item-id", data.id);
              list.append(new_item);
              list.data("max-entry",max_entry+1)
      });
}

function getTranslate() {
    var list = $("#question"); 
    var max_entry = list.data("max-entry")
    list.data("max-entry",max_entry+1)
    $.get("/testpage/test-add-q-tr/"+max_entry)
      .done(function(data) {
              item = data.html;
              var new_item = $(item);
              new_item.data("item-id", data.id);
              list.append(new_item);
              list.data("max-entry",max_entry+1)
      });
}

$(document).ready(function () {  
  $("#question").data("max-entry",0);

  $("#question-mc").click(getMultipleChoicw);
  $("#question-tr").click(getTranslate);

  var csrftoken = getCookie('csrftoken');
  $(".needcsrf").val(csrftoken);
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  });
});
