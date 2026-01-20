# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LocalizationTask(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        description: DF.SmallText | None
        end_date: DF.Date | None
        milestone: DF.Literal["Phase 1", "Phase 2", "Phase 3", "Phase 4", "Final Phase"]
        parent: DF.Data
        parentfield: DF.Data
        parenttype: DF.Data
        priority: DF.Literal["Low", "Medium", "High"]
        start_date: DF.Date | None
        status: DF.Literal["Open", "Closed", "Cancelled"]
        task: DF.Data
    # end: auto-generated types
    pass
