import json

import flet as ft
from components.reset_password import USERS, check_username, get_assets_dir
from components.terms_and_conditions import terms_and_conditions

THEME = "#0084a8"


def save_user(user: dict):
    """Add a new user and write the whole list back to users.json."""
    USERS["users"].append(user)
    with open(f"{get_assets_dir()}/data/users.json", "w") as f:
        json.dump(USERS, f, indent=2)


def register_page(page: ft.Page, on_login) -> ft.View:
    page.title = "Register Page"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    field_width = page.width * 0.4

    def text_field(hint: str, is_password: bool = False) -> ft.TextField:
        return ft.TextField(
            hint_text=hint,
            text_style=ft.TextStyle(color=THEME),
            width=field_width,
            helper_style=ft.TextStyle(color=ft.Colors.RED),
            border_radius=ft.BorderRadius.all(20),
            password=is_password,
            can_reveal_password=is_password,
        )

    def label_row(icon, text: str) -> ft.Row:
        return ft.Row(
            controls=[
                ft.Icon(icon=icon, size=25, color=THEME),
                ft.Text(text, size=20, color=THEME),
            ]
        )

    username = text_field("Username")
    fullname = text_field("Full name")
    password = text_field("*********", is_password=True)
    confirm_password = text_field("*********", is_password=True)

    errormessage = ft.Text(
        "",
        size=20,
        visible=False,
        color="#f90808",
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    terms_checkbox = ft.Checkbox(value=False)

    # ---------- helpers ----------
    def check_required(field: ft.TextField, message: str) -> bool:
        if not field.value or not field.value.strip():
            field.helper = message
            field.update()
            return False
        field.helper = None
        field.update()
        return True

    def show_error(message: str):
        errormessage.value = message
        errormessage.visible = True
        errormessage.update()

    # ---------- terms dialog ----------
    def on_terms_accept():
        terms_checkbox.value = True
        terms_checkbox.update()

    def on_terms_decline():
        terms_checkbox.value = False
        terms_checkbox.update()

    def open_terms(e):
        page.show_dialog(terms_and_conditions(page, on_terms_accept, on_terms_decline))

    # ---------- register ----------
    def register_click(e):
        errormessage.visible = False
        errormessage.update()

        # Checking each field in order, same pattern as login
        if not check_required(username, "Username can not be left empty"):
            return
        if not check_required(fullname, "Full name can not be left empty"):
            return
        if not check_required(password, "Password can not be left empty"):
            return
        if not check_required(confirm_password, "Please confirm your password"):
            return

        if password.value != confirm_password.value:
            show_error("Passwords do not match")
            return

        if check_username(username.value.strip()):
            show_error("Username is already taken")
            return

        if not terms_checkbox.value:
            show_error("You must accept the Terms and Conditions")
            return

        save_user(
            {
                "username": username.value.strip(),
                "fullname": fullname.value.strip(),
                "password": password.value,
            }
        )
        print(f"Registered {username.value}")
        on_login()

    def login_instead(e):
        on_login()

    body = ft.Container(
        expand=True,
        bgcolor=THEME,
        alignment=ft.Alignment.CENTER,
        height=page.height,
        width=page.width,
        content=ft.Container(
            height=page.height * 0.9,
            width=page.width * 0.5,
            bgcolor=ft.Colors.WHITE,
            border_radius=ft.BorderRadius.all(20),
            padding=ft.Padding.all(40),
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    # Title
                    ft.Container(
                        padding=ft.Padding(0, 10, 0, 20),
                        content=ft.Text(
                            "Register",
                            size=40,
                            weight=ft.FontWeight.BOLD,
                            color=THEME,
                        ),
                    ),
                    label_row(ft.Icons.PERSON, "Username:"),
                    username,
                    label_row(ft.Icons.BADGE, "Full name:"),
                    fullname,
                    label_row(ft.Icons.LOCK, "Password:"),
                    password,
                    label_row(ft.Icons.LOCK_OUTLINE, "Confirm password:"),
                    confirm_password,
                    # Terms and conditions
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            terms_checkbox,
                            ft.Text("I agree to the", size=15, color=THEME),
                            ft.GestureDetector(
                                content=ft.Text(
                                    "Terms and Conditions",
                                    size=15,
                                    color=THEME,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                on_tap=open_terms,
                            ),
                        ],
                    ),
                    # Error message
                    errormessage,
                    # Register button
                    ft.Container(
                        padding=ft.Padding(0, 10, 0, 0),
                        content=ft.Button(
                            content="Register",
                            bgcolor=THEME,
                            color="#FFFFFF",
                            width=page.width * 0.3,
                            height=50,
                            on_click=register_click,
                        ),
                    ),
                    # Back to login
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Already have an account?", size=15, color=THEME),
                            ft.GestureDetector(
                                content=ft.Text(
                                    "Login",
                                    size=15,
                                    color=THEME,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                on_tap=login_instead,
                            ),
                        ],
                    ),
                ],
            ),
        ),
    )
    return ft.View(
        route='/register',
        controls=[body]
    )