function light_mode() {
	document.getElementById("text_color").style.backgroundColor="white";
	document.getElementById("text_color").style.color="black";
	document.body.style.backgroundColor="white";
	document.body.style.color="black";
	var a = 0;
	var b = 0;
	while (a != 20) {
		if (b != 1000) {
			document.title= "box_light" + a;
			a++;
			b++;
		}
	}
	document.title= "Go!"
	document.getElementById("box_light").innerHTML='<button onclick="night_mode()">light-mode</button>';
}
function night_mode() {
	document.getElementById("text_color").style.backgroundColor="black";
	document.getElementById("text_color").style.color="white";
	document.body.style.backgroundColor="black";
	document.body.style.color="white";
	document.title = "Night now";
	document.getElementById("box_light").innerHTML='<button onclick="light_mode()">night-mode</button>';
}