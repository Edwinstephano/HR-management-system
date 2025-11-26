import frappe
from frappe.utils import today, add_years

def execute():
    company_name = "BSoft"
    if not frappe.db.exists("Company", company_name):
        print(f"Company {company_name} not found.")
        return

    # Check if any holiday list exists
    holiday_lists = frappe.get_all("Holiday List", filters={"docstatus": 1}, limit=1)
    
    holiday_list_name = None
    if holiday_lists:
        holiday_list_name = holiday_lists[0].name
        print(f"Found existing Holiday List: {holiday_list_name}")
    else:
        # Create a new Holiday List
        print("Creating new Holiday List...")
        try:
            holiday_list = frappe.get_doc({
                "doctype": "Holiday List",
                "holiday_list_name": "Standard Holiday List",
                "from_date": today(),
                "to_date": add_years(today(), 1),
                "weekly_off": "Sunday"
            })
            holiday_list.insert()
            holiday_list.submit()
            holiday_list_name = holiday_list.name
            print(f"Created Holiday List: {holiday_list_name}")
        except Exception as e:
            print(f"Error creating Holiday List: {e}")
            return

    # Assign to Company
    try:
        company = frappe.get_doc("Company", company_name)
        company.default_holiday_list = holiday_list_name
        company.save()
        print(f"Assigned {holiday_list_name} to Company {company_name}")
        frappe.db.commit()
    except Exception as e:
        print(f"Error updating Company: {e}")
