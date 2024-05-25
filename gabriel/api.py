import frappe
import json

from frappe.integrations.doctype.slack_webhook_url.slack_webhook_url import send_slack_message
from frappe.utils import nowdate
from frappe.utils.safe_exec import get_safe_globals

def get_context(doc):
	return {
		"doc": doc,
		"nowdate": nowdate,
		"frappe": frappe._dict(utils=get_safe_globals().get("frappe").get("utils")),
	}

@frappe.whitelist()
def send_a_slack_message(purchase_order_name):
	notification_exists = frappe.db.exists("Notification", "PO - PSVPF")
	
	if notification_exists:
		notification_doc = frappe.get_doc("Notification", notification_exists)
		
		purchase_order_doc = frappe.get_doc("Purchase Order", purchase_order_name)

		context = get_context(purchase_order_doc)
		context = {"doc": purchase_order_doc, "alert": purchase_order_doc, "comments": None}
		if purchase_order_doc.get("_comments"):
			context["comments"] = json.loads(purchase_order_doc.get("_comments"))
		
		return send_slack_message(
			webhook_url=notification_doc.slack_webhook_url,
			message=frappe.render_template(notification_doc.message, context),
			reference_doctype=purchase_order_doc.doctype,
			reference_name=purchase_order_doc.name
		)