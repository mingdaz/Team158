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

function getUpdates() {

    var qb = $("#pbody")
   
    var frm = $("#storedata")
    var max = $("#maxentry").val();
    var qnum = $("#qnum").val();
    
    if( qnum<0 || qnum <max){

       $.ajax({
      type: "POST",
      url: "/testpage/next-questions",
      data: frm.serialize(),
      success: function (data) {
          var body = $("#pbody");
          var newitem = $(data.html);
          qb.html(newitem);

          $("#maxentry").val(data.max_entry.toString());
          $("#qnum").val(data.qnum.toString());
          $("#qid").val(data.id.toString());
          $(".question-num").html(data.qnum.toString());
          var percent = (data.qnum-1)/data.max_entry*100;
          $("#processbar").attr("style","width: "+percent+"%;");
          $("#processbar").html(percent+"%");
            },
            error: function(data) {
                alert("Something went wrong!");
            }
        });

    }
    else{
   $.ajax({
      type: "POST",
      url: "/testpage/next-questions",
      data: frm.serialize(),
      success: function (data) {
          var body = $("#pbody");
          var newitem = $(data.html);
          // qb.html(newitem);
          // $("#maxentry").val(data.max_entry.toString());
          // $("#qnum").val(data.qnum.toString());
          // $("#qid").val(data.id.toString());
          body.html("");
          var percent = 100;
          $("#processbar").attr("style","width: "+percent+"%;");
          $("#processbar").html(percent+"%");
          var btn = $( ".next-btn" );
          btn.unbind( "click", getUpdates );
          btn.bind( "click", getResult );

          btn.addClass( "btn-info" );
          btn.removeClass( "btn-warning" );
          btn.html("Finish");

            },
            error: function(data) {
                alert("Something went wrong!");
            }
        });
    }
   
}


function getResult() {

   
}

$(document).ready(function () {  
  $( ".next-btn" ).bind( "click", getUpdates );
  getUpdates();
  var csrftoken = getCookie('csrftoken');
  $(".needcsrf").val(csrftoken);
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  });
});

