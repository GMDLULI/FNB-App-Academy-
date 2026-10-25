import asyncio
import flet as ft
from components.reset_password import reset_password
def login_page(page: ft.Page) -> ft.View:
    page.title = "Login Page"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    username =  ft.TextField(
                    hint_text='Username',
                    text_style=ft.TextStyle(color="#0084a8"),
                    width=page.width * 0.5,
                    helper_style=ft.TextStyle(color=ft.Colors.RED),
                    border_radius=ft.BorderRadius.all(20),
                    )

    password =  ft.TextField(
                    hint_text='*********',
                    text_style=ft.TextStyle(color="#0084a8"),
                    width=page.width * 0.5,
                    helper_style=ft.TextStyle(color=ft.Colors.RED),

                    border_radius=ft.BorderRadius.all(20),
                    password=True,
                    can_reveal_password=True,
    
    )
    errormessage = ft.Text(
                    'Invalid username or password',
                    size=25,
                    visible=False,
                    color= "#f90808",
                    weight=ft.FontWeight.BOLD
                )

    user = {
            "username" : 'User1',
            "password" : 'pas1'
        }
    
    
    def login_click(e):
        #Checking username 
        if not username.value:
            username.helper = 'Username can not be left empty'
            username.update()
            return
        else:
            username.helper=None
            username.update()
            #checking password 
        if not password.value:
            password.helper = 'Password can not be left empty'
            password.update()
            return
        else:
            password.helper=None
            password.update()
        if username.value == user["username"] and password.value == user["password"]:
            print(f'Welcome {username.value}')
            errormessage.visible = False
            errormessage.update()

        else:
            errormessage.visible = True
            errormessage.update()
    def on_register():
        asyncio.create_task(page.push_route('/register'))

    def on_forgot_password(e):
        page.show_dialog(reset_password(page))
        
  

    body = ft.Container(
        expand=True,
        bgcolor="#0084a8",
        alignment=ft.Alignment.CENTER,
        height=page.height,
        width=page.width,
        content=ft.Container(
            height=page.height * 0.85,
            width=page.width * 0.5,
            bgcolor=ft.Colors.WHITE,
            border_radius=ft.BorderRadius.all(20),
            padding=ft.Padding.all(40),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                
                controls= [
                    #login text
                   ft.Container(
                        padding = ft.Padding(0,20,0,40),
                        content=ft.Text(
                            "Login",
                            size=40,
                            weight=ft.FontWeight.BOLD,
                            color="#0084a8"
                        )
                   ),
                   # User Icon and text field
                    ft.Row(
                        controls=[
                            ft.Icon(
                                icon=ft.Icons.PERSON,
                                size=25,
                                color="#0084a8"
                            ),
                            ft.Text(
                                "Username:",
                                size=20,
                                color="#0084a8"
                            )
                        ]
                    ),
                    username,
                     ft.Row(
                        controls=[
                            ft.Icon(
                                icon=ft.Icons.MAIL,
                                size=25,
                                color="#0084a8"
                            ),
                            ft.Text(
                                "Email:",
                                size=20,
                                color="#0084a8"
                            )
                        ]
                    ),
                    password,

                    #Checkbox
                    ft.Row(
                        alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Checkbox(
                                label='Keep me logged in',
                                label_style=ft.TextStyle(color="#0084a8")
                            ),
                            ft.GestureDetector(
                                ft.Text(
                                "forgot password",
                                style=ft.TextStyle(color="#0084a8"),
                                weight=ft.FontWeight.BOLD,),
                                on_tap=on_forgot_password
                            )
                        ]
                    ),
                    # Error Message
                    errormessage,

                    #login Button
                    ft.Container(
                        padding=ft.Padding(0,20,0,0),
                        content = ft.Button(
                                content='Login',
                                bgcolor="#0084a8",
                                color="#FFFFFF",
                                width = page.width * 0.3,
                                height = 50,
                                on_click = login_click
                            )
                    ),

                    ft.Row(
                       alignment = ft.MainAxisAlignment.CENTER,
                       controls=[ 
                           ft.Text(
                            "Dont have an account?.",
                            size=15,
                            color = "#0084a8"
                        ),
                        ft.GestureDetector(
                            content = ft.Text(
                                'Create an account',
                                size=15,
                                color="#0084a8",
                                weight=ft.FontWeight.BOLD

                            ),
                            on_tap = on_register
                        )
                        ]
                    )
                    
                   
                ]
               
            )
        )
    )
    return ft.View(
            route='/login',
            controls=[body]
        )

# Run the login page independently
