frappe.ready(function () {
    frappe.web_form.validate = () => {
        const accept_terms_and_conditions = frappe.web_form.get_value(["accept_terms_and_conditions"]);

        if (!accept_terms_and_conditions) {
            frappe.msgprint(__("Please accept the terms and conditions!"));
            return false;
        }

        return true;
    };
});
