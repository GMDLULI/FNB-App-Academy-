import flet as ft

counter = 0
def increment(e):  
    global counter
    counter += 1
    e.page.controls[0].content.controls[1].value = str(counter)
    e.page.update()

def decrement(e):
    global counter
    counter -= 1
    e.page.controls[0].content.controls[1].value = str(counter)
    e.page.update()
def reset(e):
    global counter
    counter = 0
    e.page.controls[0].content.controls[1].value = str(counter)
    e.page.update()


def counter (page: ft.Page) -> ft.View:
    page.title = 'Counter'

    body = ft.Container(
        bgcolor=ft.Colors.BLACK,
        expand=True,
        height= page.height,
        width= page.width,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Counter App ", 
                        size=50, 
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD
                        ),
                ft.Text(str(counter), size=250, color=ft.Colors.YELLOW, weight=ft.FontWeight.BOLD),
                
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Button(
                            bgcolor=ft.Colors.GREEN,
                            content=ft.Icon(
                                icon=ft.Icons.ADD,
                                size=30
                                ),
                            on_click=increment, 
                            style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),),
                        ft.Button( 
                            bgcolor=ft.Colors.BLUE,
                            content=ft.Icon(
                                icon=ft.Icons.RESTORE,
                                size=30
                                ), 
                            on_click=reset,
                            style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),),
                        ft.Button( 
                            bgcolor=ft.Colors.RED,
                            content=ft.Icon(
                                icon=ft.Icons.REMOVE,
                                size=30
                                ), 
                            on_click=decrement,
                            style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),)

                        ]
                )
            ],
        )
    )
    return body
