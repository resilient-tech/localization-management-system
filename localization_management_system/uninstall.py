import click
import frappe

from localization_management_system.constants import CUSTOMIZATION
from localization_management_system.hooks import app_title as APP_NAME


def before_uninstall():
    delete_customization()

    click.secho(f"\nThank you for using {APP_NAME}!", fg="green", bold=True)


def delete_customization():
    delete_custom_fields()
    delete_property_setters()


def delete_custom_fields():
    click.secho(f"Deleting custom fields of {APP_NAME}...", fg="cyan", bold=True)

    for _, customization in CUSTOMIZATION.items():
        _delete_custom_fields(customization["custom_fields"])


def delete_property_setters():
    click.secho(f"Deleting property setters of {APP_NAME}...", fg="cyan", bold=True)

    for _, customization in CUSTOMIZATION.items():
        _delete_property_setters(customization["property_setters"])


def _delete_custom_fields(custom_fields: dict):
    """
    Delete custom fields from the given doctypes.

    :param custom_fields: Dictionary of doctypes with fields to be deleted.

    ---
    Structure of the `custom_fields` dictionary:

    ```py
    # first structure
    {
        "DocType1": ["field1", "field2", ...],
        "DocType2": ["field1", "field2", ...],
        ...
    }

    # second structure
    {
        "DocType1": [
            {"fieldname": "field1", ...},
            {"fieldname": "field2", ...},
            ...
        ],
        "DocType2": [
            {"fieldname": "field1", ...},
            {"fieldname": "field2", ...},
            ...
        ],
        ...
    }
    ```

    """
    for doctype, fields in custom_fields.items():
        fieldnames = []

        if fields and isinstance(fields, list):
            if isinstance(fields[0], str):
                fieldnames = fields
            elif isinstance(fields[0], dict):
                fieldnames = [field["fieldname"] for field in fields]

        if not fieldnames:
            continue

        frappe.db.delete(
            "Custom Field",
            {
                "fieldname": ("in", fieldnames),
                "dt": doctype,
            },
        )

        frappe.clear_cache(doctype=doctype)


def _delete_property_setters(property_setters: list[dict]):
    """
    Delete property setters.

    :param property_setters: List of property setters.
    """
    field_map = {
        "doctype": "doc_type",
        "fieldname": "field_name",
    }

    for property_setter in property_setters:
        for key, fieldname in field_map.items():
            if key in property_setter:
                property_setter[fieldname] = property_setter.pop(key)

        frappe.db.delete("Property Setter", property_setter)

        frappe.clear_cache(doctype=property_setter["doc_type"])
