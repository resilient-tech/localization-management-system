import click
import frappe
from frappe.custom.doctype.custom_field.custom_field import (
    create_custom_fields as _create_custom_fields,
)

from localization_management_system.constants import CUSTOMIZATION, MODULE_PROFILES, ROLE_PROFILES, ROLES
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
    create_roles(ROLES)
    create_role_profiles(ROLE_PROFILES)
    create_module_profiles(MODULE_PROFILES)


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


def create_roles(roles: list[dict]):
    click.secho(f"Creating roles for {APP_NAME}...", fg="cyan", bold=True)

    for role in roles:
        try:
            doc = frappe.new_doc("Role")
            doc.update(role)
            doc.save()
        except frappe.DuplicateEntryError:
            pass


# TODO: Implement the actual logic for creating profiles
def create_role_profiles(profiles: list[dict]):
    click.secho(f"Creating role profiles for {APP_NAME}...", fg="cyan", bold=True)


def create_module_profiles(profiles: list[dict]):
    click.secho(f"Creating module profiles for {APP_NAME}...", fg="cyan", bold=True)
