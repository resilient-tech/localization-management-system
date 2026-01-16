app_name = "localization_management_system"
app_title = "Localization Management System"
app_publisher = "Frappe Technologies"
app_description = "Portal for enhancing communication between Localization Builder and Frappe team"
app_email = "developers@frappe.io"
app_license = "mit"

after_install = "localization_management_system.install.after_install"
before_uninstall = "localization_management_system.uninstall.before_uninstall"

app_include_js = "localization_management_system.bundle.js"

export_python_type_annotations = True


jinja = {
    "methods": [
        "localization_management_system.localization_management_system.doctype.erpnext_localization.erpnext_localization.get_country_flag",
        "localization_management_system.localization_management_system.doctype.erpnext_localization.erpnext_localization.get_progress_pill_color",
    ],
}
