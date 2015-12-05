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

function update(){
    var list = $("#question");
    var array = list.find("li");
    for ( var i = 1; i <= array.length; i++ ) {
        var tmp = $(array[i-1]);
        tmp.find(".question-num").html(i);
    }
}

function populateList() {
    var testid = $("#testid").val();
    $.get("/testpage/get-items/"+testid)
      .done(function(data) {
          var list = $("#question");
          list.html('')
          for (var i = 0; i < data.items.length; i++) {
              item = data.items[i];
              var new_item = $(item.html);
              new_item.data("item-id", item.id);
              new_item.find('.save-btn').click(btnsave);
              new_item.find('.delete-btn').click(btndelete);
              new_item.find('.edit-btn').click(btnedit);
              list.append(new_item);
          }
          update();
      });
}


function postmytest(){
    var list = $("#question");
    var array = list.find("li");
    if(array.length==0){
      alert("You don't have any question, create some questions")
      return
    }    
    if(list.find(".save-btn").length>0){
      alert("You have unsave question, please save all questions and then post")
      return
    } 

    var testid = $("#testid").val();
    var flag = 1;

    $.ajax({
            type: "POST",
            url: "/testpage/test-level/"+testid,
            success: function (data) {                
            },
            error: function(data) {
                flag = 0
                alert("Something went wrong!");
            }
    });

    $.ajax({
            type: "POST",
            url: "/testpage/test-post/"+testid,
            success: function (data) {
                                
            },
            error: function(data) {
                flag = 0
                alert("Something went wrong!");
            }
    });
    
    if(flag==1){
      var tmp = list.parent();
      list.remove();
      tmp.parent().find(".btn").prop('disabled', true);  
      tmp.html("Create test success!")
    }
        
}

function getMultipleChoice() {
    var list = $("#question"); 
   $.ajax({
    type: "POST",
    url: "/testpage/test-add-q-mc",
    data: $("#testidform").serialize(),
    success: function (data) {
      console.log("success")
              item = data.html;
              var new_item = $(item);
              new_item.find('.save-btn').click(btnsave);
              new_item.find('.delete-btn').click(btndelete);
              new_item.data("item-id", data.id);
              list.append(new_item);
              update()
    },
    error: function(data) {
      flag = 0;
      console.log("error")
    }
    });
}

function getTranslate() {
    var list = $("#question"); 
   $.ajax({
    type: "POST",
    url: "/testpage/test-add-q-tr",
    data: $("#testidform").serialize(),
    success: function (data) {
      console.log("success")

              item = data.html;
              var new_item = $(item);
              
              new_item.find('.save-btn').click(btnsave);
              new_item.find('.delete-btn').click(btndelete);
              
              new_item.data("item-id", data.id);
              list.append(new_item);
              update()
      
    },
    error: function(data) {
      flag = 0;
      console.log("error")
    }
    });
}

function btnsave()
{
    var frm = $(event.target).parent().parent().parent();
    var list = frm.parent();
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function (data) {
                frm.html($(data.html).find('.panel'));
                frm.find('.delete-btn').click(btndelete);
                
                var btn = list.find('.save-btn');
                if(data.flag==1){
                  btn.removeClass( "save-btn" );
                  btn.addClass( "edit-btn" );
                  btn.removeClass( "btn-info" );
                  btn.addClass( "btn-warning" );
                  btn.html("Edit");
                  btn.click(btnedit);       
                  list.find("input").prop('disabled', true);  
                }
                else{
                  btn.click(btnsave)
                }
                update();
            },
            error: function(data) {
                alert("Something went wrong!");
            }
        });
}

function btnedit()
{
    var id = $(event.target).parent().parent().parent().parent().data("item-id");
    var btn = $(event.target);
    var frm = $(event.target).parent().parent().parent();
    btn.removeClass( "edit-btn" );
    btn.addClass( "save-btn" );
    btn.addClass( "btn-info" );
    btn.removeClass( "btn-warning" );
    btn.html("Save");
    btn.unbind("click",btnedit);
    btn.click(btnsave);
    frm.find("input").prop('disabled', false);
    $.ajax({
            type: 'POST',
            url: '/testpage/test-edit-question/'+id,
            success: function (data) {
              update();
            },
            error: function(data) {
                alert("Something went wrong!");
            }
        });
}

function btndelete()
{
    var id = $(event.target).parent().parent().parent().parent().data("item-id");
    var rm = $(event.target).parent().parent().parent().parent()
    $.ajax({
            type: 'POST',
            url: '/testpage/test-delete-question/'+id,
            success: function (data) {
              rm.remove();
              update();
            },
            error: function(data) {
                alert("Something went wrong!");
            }
        });
    
}

$(document).ready(function () {  
  // $("#question").data("max-entry",0);

  $("#question-mc").click(getMultipleChoice);
  $("#question-tr").click(getTranslate);
  $("#posttest").click(postmytest);

  var csrftoken = getCookie('csrftoken');
  $(".needcsrf").val(csrftoken);
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  });

  populateList();

});

