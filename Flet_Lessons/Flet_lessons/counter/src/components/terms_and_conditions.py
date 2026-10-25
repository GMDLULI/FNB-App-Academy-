import flet as ft

THEME = "#0084a8"

TERMS = [
    (
        "1. Acceptance of Terms",
        "By creating an account you confirm that you have read, understood and "
        "agree to be bound by these Terms and Conditions.",
    ),
    (
        "2. Eligibility",
        "You must provide accurate and complete information when registering. "
        "You are responsible for keeping your account details up to date.",
    ),
    (
        "3. Account Security",
        "You are responsible for keeping your username and password confidential "
        "and for all activity that happens under your account. Notify us "
        "immediately if you suspect unauthorised access.",
    ),
    (
        "4. Acceptable Use",
        "You agree not to misuse the service, attempt to gain unauthorised access "
        "to other accounts or systems, or use the service for unlawful purposes.",
    ),
    (
        "5. Privacy",
        "We collect and store the information you provide (such as your name and "
        "username) only to operate your account. We will not sell your personal "
        "information to third parties.",
    ),
    (
        "6. Termination",
        "We may suspend or terminate your account if you breach these Terms. "
        "You may stop using the service and request deletion of your account at "
        "any time.",
    ),
    (
        "7. Changes to These Terms",
        "We may update these Terms from time to time. Continued use of the "
        "service after changes means you accept the updated Terms.",
    ),
]


def terms_and_conditions(page: ft.Page, on_accept, on_decline) -> ft.AlertDialog:
    """Modal dialog listing the terms. Calls on_accept() or on_decline() when closed."""

    def accept_click(e):
        page.pop_dialog()
        on_accept()

    def decline_click(e):
        page.pop_dialog()
        on_decline()

    sections = []
    for heading, body in TERMS:
        sections.append(
            ft.Column(
                spacing=4,
                controls=[
                    ft.Text(heading, weight=ft.FontWeight.BOLD, color=THEME, size=16),
                    ft.Text(body, size=14),
                ],
            )
        )

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Terms and Conditions", weight=ft.FontWeight.BOLD, color=THEME),
        content=ft.Container(
            width=500,
            height=350,
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                spacing=16,
                controls=sections,
            ),
        ),
        actions=[
            ft.Button(content="Decline", on_click=decline_click),
            ft.Button(
                content="Accept",
                bgcolor=THEME,
                color="#FFFFFF",
                on_click=accept_click,
            ),
        ],
    )
    return dialog