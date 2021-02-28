/*alert("Good")*/
function question(){
    var d = document.getElementById("answer_one").value;
    if (d ==3)  {
      document.getElementById("meta_answer").innerHTML="Oh, habeís iniciado bien";
    }
    else if (d < 1000000 || d > 1000000){
      document.getElementById("meta_answer").innerHTML="Te equivocaste, ¡genial!";
    }
    if (d == false){
      document.getElementById("meta_answer").innerHTML=" ";
    }
   }