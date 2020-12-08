/* Credit: https://www.w3schools.com/howto/howto_js_dropdown.asp */
if($(window).width() < 1000) {
	function dropdownfunc() {
		document.getElementById("topnav").classList.toggle("show");
	}
	window.onclick = function(event) {
		if(!event.target.matches('button')) {
			document.getElementByTagName("nav").remove("show");
		}
	}
}