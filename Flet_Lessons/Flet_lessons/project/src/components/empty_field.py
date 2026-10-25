import flet as ft


def empty_field(page:ft.Page):
    
    def on_continue(e):
        page.pop_dialog()


    model = ft.AlertDialog(
            title='Please enter your username',
            modal=True,
            actions=[
            ft.Button(
                content='Continue',
                on_click=on_continue
            ),])
    return model
     