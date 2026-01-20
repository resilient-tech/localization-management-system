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

        from localization_management_system.localization_management_system.doctype.localization_task.localization_task import (
            LocalizationTask,
        )

        accept_terms_and_conditions: DF.Check
        applicable_for: DF.Literal["Accounting", "HR"]
        assigned_enabler: DF.Link | None
        assigned_reviewer: DF.Link | None
        company_name: DF.Data | None
        company_website: DF.Data | None
        country: DF.Link
        country_code: DF.Data | None
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
        progress_status: DF.Literal[
            "Submitted",
            "Pending Review",
            "Shortlisted Partner",
            "In Progress",
            "Development Started",
            "Development Completed",
            "Testing Completed",
            "Listed on Frappe Cloud",
            "Auto-install Enabled on FC",
            "Abandoned",
            "Archived",
        ]
        proposal: DF.Attach | None
        published_date: DF.Date | None
        remarks: DF.SmallText | None
        repo: DF.Data | None
        repo_permission_granted: DF.Literal["Yes", "No"]
        repo_visibility: DF.Literal["", "Public", "Private"]
        route: DF.Data | None
        status: DF.Literal["Open", "Replied", "Pending", "Cancelled"]
        subject: DF.Data
        tasks: DF.Table[LocalizationTask]
    # end: auto-generated types

    # TODO: After release
    # def before_insert(self):
    #     self.create_desk_user()
    #     self.owner = self.developer_mail
    #     self.modified_by = self.developer_mail

    def validate(self):
        super().validate()

        if not self.accept_terms_and_conditions:
            frappe.throw(
                {
                    "message": _("Please accept the Terms and Conditions to proceed."),
                    "title": _("Terms and Conditions"),
                }
            )

    # TODO: After release
    # def create_desk_user(self):
    #     if not self.developer_mail or frappe.db.exists("User", self.developer_mail):
    #         return

    #     PROFILE = "Localization Developer"

    #     user = frappe.new_doc("User")

    #     user.update(
    #         {
    #             "email": self.developer_mail,
    #             "first_name": self.full_name.split(" ")[0],
    #             "send_welcome_email": 1,
    #             "module_profile": PROFILE,
    #             "list_sidebar": 0,
    #             "bulk_actions": 0,
    #             "view_switcher": 0,
    #             "form_sidebar": 0,
    #             "dashboard": 0,
    #         }
    #     )

    #     user.add_roles([PROFILE, "Inbox User"])

    #     user.flags.ignore_permissions = True
    #     user.insert(ignore_permissions=True)


#### Utility functions for Jinja templates ####
def get_country_flag(country_code: str, width: int = 20, height: int = 15) -> str:
    """
    Returns the URL of the country flag image based on the country code.
    """
    return f'<img src="https://flagcdn.com/{country_code}.svg" width="{width}" height="{height}" alt="{country_code} flag">'


def get_progress_pill_color(progress_status: str) -> str:
    """
    Returns the CSS class for the progress pill based on the progress status.
    """
    if not progress_status:
        return "orange"

    status_colors = {
        "Submitted": "blue",
        "Pending Review": "grey",
        "Shortlisted Partner": "orange",
        "In Progress": "orange",
        "Development Started": "blue",
        "Development Completed": "green",
        "Testing Completed": "yellow",
        "Listed on Frappe Cloud": "green",
        "Auto-install Enabled on FC": "green",
        "Abandoned": "red",
        "Archived": "orange",
    }

    return status_colors.get(progress_status, "orange")


#### Web View Context Functions ####
def get_localizations_list(
    doctype,
    txt=None,
    filters=None,
    limit_start=0,
    limit_page_length=20,
    order_by=None,
):
    EL = frappe.qb.DocType("ERPNext Localization")

    # Build query
    query = (
        frappe.qb.from_(EL)
        .select(
            EL.name,
            EL.route,
            EL.subject,
            EL.country,
            EL.country_code,
            EL.applicable_for,
            EL.description,
            EL.progress_status,
            EL.estimated_completion_date,
            EL.repo,
            EL.documentation_url,
            EL.marketplace_url,
            EL.company_name,
            EL.company_website,
        )
        .where(EL.enable_webview == 1)
        .orderby(EL.country)
        .orderby(EL.company_name)
        .orderby(EL.subject)
        .orderby(EL.progress_status)
        .limit(limit_page_length)
        .offset(limit_start)
    )

    return query.run(as_dict=True)


def get_list_context(context=None):
    context.update(
        {
            "show_search": True,
            "no_breadcrumbs": True,
            "get_list": get_localizations_list,
            "title": "ERPNext Localizations",
        }
    )
