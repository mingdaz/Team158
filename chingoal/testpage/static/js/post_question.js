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
    list.data("max-entry",array.length);
}
//     <script>
// function display( divs ) {
//   var a = [];
//   for ( var i = 0; i < divs.length; i++ ) {
//     a.push( divs[ i ].innerHTML );
//   }
//   $( "span" ).text( a.join(" ") );
// }
// display( $( "div" ).get().reverse() );
// </script>


function getMultipleChoicw() {
    var list = $("#question"); 
    var max_entry = list.data("max-entry")
   
    $.get("/testpage/test-add-q-mc/"+max_entry)
      .done(function(data) {
              item = data.html;
              var new_item = $(item);
              
              new_item.find('.save-btn').click(btnsave);
              new_item.find('.delete-btn').click(btndelete);
              
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
              
              new_item.find('.save-btn').click(btnsave);
              new_item.find('.delete-btn').click(btndelete);

              new_item.data("item-id", data.id);
              list.append(new_item);
              list.data("max-entry",max_entry+1)
      });
}

function btnsave()
{
    var btn = $(event.target);
    btn.removeClass( "save-btn" );
    btn.addClass( "edit-btn" );
    btn.removeClass( "btn-info" );
    btn.addClass( "btn-warning" );
    btn.html("Edit");
    btn.unbind("click",btnsave);
    btn.click(btnedit);
}

function btnedit()
{
    var btn = $(event.target);
    btn.removeClass( "edit-btn" );
    btn.addClass( "save-btn" );
    btn.addClass( "btn-info" );
    btn.removeClass( "btn-warning" );
    btn.html("Save");
    btn.unbind("click",btnedit);
    btn.click(btnsave);
}

function btndelete()
{
    var btn = $(event.target).parent().parent().parent().remove();
    update();
}

$(document).ready(function () {  
  $("#question").data("max-entry",0);

  $("#question-mc").click(getTranslate);
  $("#question-tr").click(getMultipleChoicw);

  var csrftoken = getCookie('csrftoken');
  $(".needcsrf").val(csrftoken);
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  });
});
