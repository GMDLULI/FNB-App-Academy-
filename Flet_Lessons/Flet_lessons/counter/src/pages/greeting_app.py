import flet as ft


def greeting(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    username =  ft.TextField(
                        hint_text='Your name',
                        text_style=ft.TextStyle(color="#d01eb8"),
                        width=page.width * 0.5,
                        helper_style=ft.TextStyle(color=ft.Colors.RED),
                        border_radius=ft.BorderRadius.all(20),
                        visible=True
                        )
    user_info = ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                visible = True,
                controls = [
                    ft.Icon(
                        icon=ft.Icons.PERSON,
                        size=25,
                        color="#d01eb8"
                    ),
                    ft.Text(
                        'Please Enter you Full name',
                        size = 15,
                        color="#d01eb8"
                    ), 
                ],
                                    
            )
    greet = ft.Text(
            '',
            size=25,
            visible=False,
            color= "#d01eb8",
            weight=ft.FontWeight.BOLD
    )
    button_text = ft.Text("Greet me")
   

    
    
    def greet_click(e):
        # If the greeting is currently visible, return to the input state
        if greet.visible:
            greet.visible = False
            username.visible = True
            user_info.visible = True

            username.value = ""
            username.helper = None

            button_text.value = "Greet me"

        else:
            # Validate the entered name
            if not username.value or not username.value.strip():
                username.helper = "Username cannot be left empty"
                username.update()
                return

            # Display the greeting
            username.helper = None
            greet.value = f"Hello {username.value.strip()}!"

            username.visible = False
            user_info.visible = False
            greet.visible = True

            button_text.value = "Enter another name"
            button_text.update()

        # Refresh the changed components
        username.update()
        user_info.update()
        greet.update()
        button_text.update()

    greet_button = ft.Container(
                    padding=ft.Padding(0,20,0,0),
                    content=ft.Button(
                        content=button_text,
                        bgcolor="#d01eb8",
                        color = "#FFFFFF",
                        width= page.width * 0.3,
                        height = 55,
                        on_click=greet_click
                    )
                )

           

    body = ft.Container(
       expand=True,
       alignment=ft.Alignment.CENTER,
       bgcolor= ft.Colors.WHITE,
       content=ft.Column(
           alignment=ft.MainAxisAlignment.CENTER,
           horizontal_alignment=ft.CrossAxisAlignment.CENTER, 

           controls=[
               user_info,
               username,
               greet,
               greet_button
           ]
       )

    )

    page.add(body)

ft.run(greeting)
