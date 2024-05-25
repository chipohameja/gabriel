# Copyright (c) 2024, Chipo Hameja and contributors
# For license information, please see license.txt

import frappe
import os
from frappe.model.document import Document


class FontSettings(Document):
	def before_save(self):
		frappe.errprint("Publishing realtime")
		frappe.publish_realtime('set_font', {'font': self.selected_font})
		frappe.errprint("Published realtime")

		frappe.local.cookie_manager.set_cookie("font", self.selected_font)

		cwd = os.path.realpath(os.path.dirname(__file__)) # = os.getcwd()
		frappe.errprint(cwd)
		
		modified_text = remove_text_after_third_slash(cwd)
		frappe.errprint(modified_text)

		new_path = modified_text + "/public/css/style.css"
		set_font(new_path)

def remove_text_after_third_slash(text):
	parts = text.rsplit('/', 3)  # Split the text into parts using '/' as delimiter, starting from the right side, and limit to 4 parts
	if len(parts) > 3:
		return '/'.join(parts[:-2])  # Join the first three parts together, omitting the last two parts
	else:
		return text  # Return the original text if there are less than 4 parts
	
def set_font(css_path):
	linenr = 1
	with open(css_path) as mycss:
		mylist = mycss.readlines()
	
	# list numbering starts at 0
	# line 1 is mylist[0]
	my_line = linenr - 2
	the_line = mylist[my_line]
	the_new_line = the_line.replace('font-family: cursive;', 'font-family: fantasy;')
	mylist[my_line] = the_new_line
	mystring = ''.join(mylist)
	with open(css_path, 'w') as mycss:
		mycss.write(mystring)