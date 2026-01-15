# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt


import frappe
from frappe import _
from frappe.website.website_generator import WebsiteGenerator


class ERPNextLocalization(WebsiteGenerator):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        accept_terms_and_conditions: DF.Check
        applicable_for: DF.Literal["Accounting", "HR"]
        assigned_enabler: DF.Link | None
        assigned_reviewer: DF.Link | None
        company_name: DF.Data | None
        company_website: DF.Data | None
        country: DF.Link
        description: DF.SmallText
        developer_github: DF.Data | None
        developer_mail: DF.Data
        documentation_url: DF.Data | None
        enable_webview: DF.Check
        estimated_completion_date: DF.Date | None
        full_name: DF.Data
        is_partner: DF.Check
        marketplace_url: DF.Data | None
        naming_series: DF.Literal["ERP-LOC-.YYYY.-"]
        partner: DF.Link | None
        progress_status: DF.Literal[
            "",
            "Shortlisted Partner",
            "Development Started",
            "Development Completed",
            "Testing Completed",
            "Listed on Frappe Cloud",
            "Auto-install Enabled on FC",
        ]
        proposal: DF.Attach | None
        published_date: DF.Date | None
        remarks: DF.SmallText | None
        repo: DF.Data | None
        repo_permission_granted: DF.Literal["Yes", "No"]
        repo_visibility: DF.Literal["", "Public", "Private"]
        route: DF.Data | None
        status: DF.Literal["Open", "Replied", "Pending", "Cancelled"]
        title: DF.Data
    # end: auto-generated types

    def before_insert(self):
        self.create_desk_user()
        self.owner = self.developer_mail
        self.modified_by = self.developer_mail

    def validate(self):
        super().validate()

        if not self.accept_terms_and_conditions:
            frappe.throw(
                {
                    "message": _("Please accept the Terms and Conditions to proceed."),
                    "title": _("Terms and Conditions"),
                }
            )

    def create_desk_user(self):
        if not self.developer_mail or frappe.db.exists("User", self.developer_mail):
            return

        PROFILE = "Localization Developer"

        user = frappe.new_doc("User")

        user.update(
            {
                "email": self.developer_mail,
                "first_name": self.full_name.split(" ")[0],
                "send_welcome_email": 1,
                "module_profile": PROFILE,
                "list_sidebar": 0,
                "bulk_actions": 0,
                "view_switcher": 0,
                "form_sidebar": 0,
                "dashboard": 0,
            }
        )

        user.add_roles([PROFILE, "Inbox User"])

        user.flags.ignore_permissions = True
        user.insert(ignore_permissions=True)
