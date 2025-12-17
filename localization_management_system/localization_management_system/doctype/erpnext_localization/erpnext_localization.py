# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ERPNextLocalization(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        applicable_for: DF.Literal["Accounting", "HR"]
        apply_to_review_localization_to_govt: DF.Literal["", "Yes", "No"]
        assigned_enabler: DF.Link | None
        assigned_reviewer: DF.Link | None
        builder_mail: DF.Data
        company_name: DF.Data | None
        company_website: DF.Data | None
        country: DF.Link
        country_have_policy_for_open_source: DF.Literal["", "Yes", "No"]
        description: DF.SmallText | None
        documentation_url: DF.Data | None
        estimated_completion_date: DF.Date | None
        govt_has_approved_localization: DF.Literal["", "Yes", "No"]
        have_identified_influence_person_to_influence: DF.Literal["", "Yes", "No"]
        is_partner: DF.Check
        is_published: DF.Check
        letter_send_to_govt: DF.Attach | None
        marketplace_url: DF.Data | None
        naming_series: DF.Literal["ERP-LOC-.YYYY.-"]
        open_source_policy_doc: DF.Data | None
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
        published_date: DF.Date | None
        remarks: DF.SmallText | None
        repo: DF.Data | None
        repo_permission_granted: DF.Literal["Yes", "No"]
        repo_visibility: DF.Literal["", "Public", "Private"]
        status: DF.Literal["Open", "Replied", "Pending", "Cancelled"]
        title: DF.Data
    # end: auto-generated types
    pass
