    function unlock(id, unlock) {
        var val = parseInt(document.getElementById(id).value,10);
        if ((val - unlock) > 1) {
            alert("Please unlock in order!");
        } else {
            var r = confirm("Do you want to unlock lesson "+val+"?");
            if (r == true) {
                location.href = "unlock-learning/"+val;
            }
        }
    }
