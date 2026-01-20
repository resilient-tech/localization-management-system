// Copyright (c) 2025, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("ERPNext Localization", {
    refresh(frm) {
        if (frm.is_new()) return;

        frm.trigger("add_publish_web_view_button");
    },

    add_publish_web_view_button(frm) {
        frm.add_custom_button(
            frm.doc.enable_webview ? __("Unpublish Web View") : __("Publish Web View"),
            () => {
                frm.set_value("enable_webview", !frm.doc.enable_webview);
                frm.save();
            }
        );
    },

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
