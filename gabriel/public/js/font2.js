if (frappe.require) {
	console.log("1")

	console.log("frappe is: ", frappe)
} else {
	frappe.ready(function () {
		console.log(2)
	});
}