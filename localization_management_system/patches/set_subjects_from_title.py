import frappe


def execute():
    EL = frappe.qb.DocType("ERPNext Localization")
    frappe.qb.update(EL).set(EL.subject, EL.title).run()
