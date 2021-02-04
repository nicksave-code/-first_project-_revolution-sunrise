/*alert("Good")*/
function doc(){
    var d = document.getElementById("here_mind").value;
    if (d.length == 0) {
      d = 0;
    }
    document.getElementById("newHelp").innerHTML= `${d} C° is equal to ${(9 / 5) * d + 32} F°`;
   }