import click
import frappe
from frappe.custom.doctype.custom_field.custom_field import (
    create_custom_fields as _create_custom_fields,
)

from localization_management_system.constants import CUSTOMIZATION
from localization_management_system.hooks import app_title as APP_NAME

POST_INSTALL_PATCHES = []


def after_migrate():
    if frappe.get_conf().get("developer_mode"):
        setup_customization()


def after_install():
    setup_customization()
    run_post_install_patches()

    click.secho(f"\n{APP_NAME} installed successfully!", fg="green", bold=True)


def setup_customization():
    create_custom_fields()
    create_property_setters()


def run_post_install_patches():
    if not POST_INSTALL_PATCHES:
        return

    click.secho("Running post-install patches...", fg="yellow")

    frappe.flags.in_patch = True

    try:
        for patch in POST_INSTALL_PATCHES:
            patch_module = f"localization_management_system.patches.post_install.{patch}.execute"
            frappe.get_attr(patch_module)()

    finally:
        frappe.flags.in_patch = False


def create_custom_fields():
    click.secho(f"Creating custom fields for {APP_NAME}...", fg="cyan", bold=True)

    for module, customization in CUSTOMIZATION.items():
        _add_module(customization["custom_fields"], module)
        _create_custom_fields(customization["custom_fields"])


def create_property_setters():
    click.secho(f"Creating property setters for {APP_NAME}...", fg="cyan", bold=True)

    for module, customization in CUSTOMIZATION.items():
        _create_property_setters(customization["property_setters"], module)


def _create_property_setters(property_setters: list, module: str):
    for props in property_setters:
        frappe.make_property_setter(props, module=module)


def _add_module(custom_fields: dict, module: str):
    for fields in custom_fields.values():
        for field in fields:
            field["module"] = module
