//if (frappe.get_cookie("font")) { }
const elements = document.querySelector("body *");

console.log("Trying to get cookie")

elements.style.fontFamily = frappe.get_cookie("font");

console.log("Gotten cookie")

frappe.realtime.on('set_font', (data) => {
	console.log(data)
})