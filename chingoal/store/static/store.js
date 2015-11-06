    var = LEVELS["One level","Two levels","Three levels","Four levels","Five levels"];
    document.getElementById("myButton1").onclick = function () {
        var r=confirm("Do you want to unlock lesson 1?");
        if (r==true) {
            location.href = "unlock-learning/LEVELS[0]";
        }       
    };
    document.getElementById("myButton2").onclick = function () {
        var r=confirm("Do you want to unlock lesson 2?");
        if (r==true) {
            location.href = "unlock-learning/LEVELS[1]";
        }       
    };
    document.getElementById("myButton3").onclick = function () {
        var r=confirm("Do you want to unlock lesson 3?");
        if (r==true) {
            location.href = "unlock-learning/LEVELS[2]";
        }       
    };
    document.getElementById("myButton4").onclick = function () {
        var r=confirm("Do you want to unlock lesson 4?");
        if (r==true) {
            location.href = "unlock-learning/LEVELS[3]";
        }       
    };
    document.getElementById("myButton5").onclick = function () {
        var r=confirm("Do you want to unlock lesson 5?");
        if (r==true) {
            location.href = "unlock-learning/LEVELS[4]";
        }       
    };
