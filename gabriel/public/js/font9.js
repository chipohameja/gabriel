//if (frappe.get_cookie("font")) { }
const elements = document.querySelector("body *");

console.log("Trying to get cookie")

elements.style.fontFamily = frappe.get_cookie("font");

console.log("Gotten cookie")

function set_rq() {
	frappe.realtime.on('set_font', (data) => {
		console.log(data)
	})

	console.log("Listener added")
}

set_rq();

console.log("Setup realtime")