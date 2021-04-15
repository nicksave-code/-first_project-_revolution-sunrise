function name_answer() {
   var name_input = document.getElementById("input_math").value;
	name_input = name_input.toLowerCase();

var friends = [
   ["nico", "nicolas", "sand", "sandra"],
	[17, 18]
]

	if (name_input == friends[0][0] || name_input == friends[0][1]) {
		document.getElementById("box_answer_name").innerHTML="Hey, friend " + name_input;
   }
   else if (name_input == friends[0][2] || name_input == friends[0][3]) {
      document.getElementById("box_answer_name").innerHTML='<audio controls><source src="Lindsey.mp3" type="audio/mpeg"></audio>';
   }
   else {
      document.getElementById("box_answer_name").innerHTML = "";
   }
}
function age_color() {
   document.getElementById("age_2010").style.color="black";
   document.getElementById("age_2010").style.backgroundColor="white";
}
function mayor_color() {
   document.getElementById("mayor_edad").style.color="black";
   document.getElementById("mayor_edad").style.backgroundColor="white";
}