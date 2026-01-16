// Copyright (c) 2025, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("ERPNext Localization", {
    get_email_recipients(frm, type) {
        if (type !== "recipients") return [];

        return frm.doc.developer_mail ? [frm.doc.developer_mail] : [];
    },

    validate(frm) {
        if (!frm.doc.accept_terms_and_conditions) {
            frappe.throw({
                message: __("Please accept the Terms and Conditions to proceed."),
                title: __("Terms and Conditions"),
            });
        }
    },
});
