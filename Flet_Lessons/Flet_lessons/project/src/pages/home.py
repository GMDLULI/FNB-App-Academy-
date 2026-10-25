import asyncio
import json
import os
from pathlib import Path
import flet as ft
from components.empty_field import empty_field
from pages.greet import greet_page

def home_page(page: ft.Page) -> ft.View:
    username =  ft.TextField(
                    hint_text='Username',
                    text_style=ft.TextStyle(color="#820590"),
                    width=page.width * 0.5,
                    helper_style=ft.TextStyle(color=ft.Colors.RED),
                    border_radius=ft.BorderRadius.all(20),
                    )


    def next_page():

        if username.value:
            page.session.store.set("username", username.value)
            # page.views.append(greet_page(page, username.value))
            asyncio.create_task(page.push_route('/greeting'))
        else:
            page.show_dialog(empty_field(page))
            
    

    continue_button = ft.Container(
                    padding=ft.Padding(0,20,0,0),
                    content=ft.Button(
                        content='Continue',
                        bgcolor="#820590",
                        color = "#FFFFFF",
                        width= page.width * 0.3,
                        height = 55,
                        on_click= next_page
                    )
                )

    body = ft.Container(
        expand=True,
        alignment=ft.Alignment.CENTER,
        bgcolor="#820590",

        content=ft.Container(
            bgcolor=ft.Colors.WHITE,
            border_radius=ft.BorderRadius.all(20),
            height=page.height *0.7,
            width= page.width * 0.5,
            padding=ft.Padding.all(40),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls= [
                   ft.Container(
                        padding = ft.Padding(0,20,0,40),
                        alignment = ft.Alignment.CENTER,
                        content=ft.Text(
                            "Welcome Please enter you username",
                            size=40,
                            weight=ft.FontWeight.BOLD,
                            color="#820590"
                        )
                    
                   ),
                   ft.Row(
                        controls=[
                                ft.Icon(
                                    icon=ft.Icons.PERSON,
                                    size=25,
                                    color="#820590"
                                ),
                                ft.Text(
                                    "Username:",
                                    size=20,
                                    color="#820590"
                                )
                            ]
                   ),
                   username,
                   continue_button
                   ]

            )
        )
    )
    return ft.View(
          route='/',
          controls=[body]
    )
    
       
    
    
    
