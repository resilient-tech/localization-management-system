import frappe


def execute():
    EL = frappe.qb.DocType("ERPNext Localization")

    frappe.qb.update(EL).set(EL.progress_status, "Submitted").where(
        (EL.progress_status.isnull()) | (EL.progress_status == "")
    ).run()
