import flet as ft

def greet_page(page:ft.Page, user) -> ft.View:

    async def next_page():
        await page.push_route('/home')
     
    back_button = ft.Container(
                        padding=ft.Padding(0,20,0,0),
                        content=ft.Button(
                            content='Back',
                            bgcolor="#820590",
                            color = "#FFFFFF",
                            width= page.width * 0.3,
                            height = 55,
                            on_click= next_page
                        )
                    )
    welcome_text = ft.Text(
                    f'Welcome {user}!',
                    size=25,
                    color="#820590",
                    weight=ft.FontWeight.BOLD

                )
    body = ft.Container(
         expand=True,
                alignment=ft.Alignment.CENTER,
                bgcolor=ft.Colors.WHITE,
                content=ft.Container(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls= [
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls= [
                                    ft.Icon(
                                    ft.CupertinoIcons.PROFILE_CIRCLED,
                                    color="#820590",
                            ),
                             welcome_text,
                             ]
                            ),
                           
                            back_button
                            ]

                    )
                    
                )
    )
    return ft.View(
        route='/greeting',
        controls=[body]
    )