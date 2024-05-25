frappe.ready(function () {
	if (localStorage.getItem("font")) {}
	const elements = document.querySelector("body *");

	elements.style.fontFamily = frappe.get_cookie("font");

	frappe.realtime.on('set_font', (data) => {
		console.log(data)
	})
})