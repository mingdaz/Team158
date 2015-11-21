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
    var list = $("#gstream")
    var max_entry = list.data("max-entry")
    $.get("/grumblr/get-changes/"+ max_entry)
      .done(function(data) {
          list.data('max-entry', data['max-entry']);
          for (var i = 0; i < data.items.length; i++) {
              item = data.items[i];
              var new_item = $(item.html);
              new_item.data("item-id", item.id);
              list.prepend(new_item);
          }
            $(".addbtn").click(commentPost);
      });
}

function btnnext(){
    var list = $("#question");
    var array = list.find("li");
    
    if(array.length==0){
      alert("You don't have any question, create some questions")
      return
    }    
    if(list.find(".next-btn").length>0){
      alert("You have unsave question, please save all questions and then post")
      return
    } 
    $.ajax({
            type: "POST",
            url: "/testpage/get-test-post-id",
            success: function (data) {
                var id;
                var flag = 1;
                for ( var i = 1; i <= array.length; i++ ) {
                    id = $(array[i-1]).data("item-id");
                        $.ajax({
                          type: "POST",
                          url: "/testpage/test-post/"+data.id+"/"+id,
                          success: function (data) {
                            console.log("success")
                          },
                          error: function(data) {
                            flag = 0;
                            console.log("error")
                          }
                      });                    
                }
                if(flag==1){
                  var tmp = list.parent();
                  list.remove();
                  tmp.parent().find(".btn").prop('disabled', true);  
                  tmp.html("Create test success!")
                }
                
            },
            error: function(data) {
                alert("Something went wrong!");
            }
    });
        
    }



$(document).ready(function () {  
  $("#nextbtn").click(postmytest);
  getUpdates();
  var csrftoken = getCookie('csrftoken');
  $(".needcsrf").val(csrftoken);
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  });
});

