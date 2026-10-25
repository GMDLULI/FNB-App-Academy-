import json
import os
from pathlib import Path

import flet as ft

def get_assets_dir() -> Path:
    default_assets_dir = Path(__file__).parent / "assets"   # fallback for local runs
    return Path(os.environ.get("FLET_ASSETS_DIR", str(default_assets_dir))).resolve()

def load_file():
    default_path = get_assets_dir()
    with open(f'{default_path}/data/users.json', 'r') as f:
        return json.load(f)

USERS = load_file()

def update_user(user):
    for i , exsiting in enumerate(USERS['users']):
        if exsiting['username'] == user['username']:
            USERS['users'][i] = user
            break
    default_path = get_assets_dir()
    with open(f'{default_path}/data/users.json', 'w') as f:
        return json.dump(USERS, f, indent=2)

def check_username(username):
    for user in USERS['users']:
        if user['username'].lower() == username.lower():
            return user
    return None



def reset_password(page: ft.Page):
    username =  ft.TextField(
                    hint_text='Username',
                    helper_style=ft.TextStyle(color=ft.Colors.RED),
                    border_radius=ft.BorderRadius.all(20),
                ) 
    password = ft.TextField(
                    hint_text='Password',
                    password=True,
                    helper_style=ft.TextStyle(color=ft.Colors.RED),
                    border_radius=ft.BorderRadius.all(20),
                )
    confirm_password = ft.TextField(
                    hint_text='Confirm Password',
                    password=True,
                    helper_style=ft.TextStyle(color=ft.Colors.RED),
                    border_radius=ft.BorderRadius.all(20),
                )
    errormessage = ft.Text(
                        'Username not found',
                        size=25,
                        visible=False,
                        color= "#f90808",
                        weight=ft.FontWeight.BOLD
                    )
    def on_cancel(e):
        page.pop_dialog()
        page.update()


    def on_save(e):
            if not password.value:
                password.helper = 'Password can not be left empty'
                password.update()
                return
            else:
                password.helper=None
                password.update()
            if not confirm_password.value:
                confirm_password.helper = 'Password can not be left empty'
                confirm_password.update()
                return
            else:
                confirm_password.helper=None
                confirm_password.update()
    
            if password != confirm_password:
                errormessage.visible = True
                errormessage.value = "Passwords do not match"
                errormessage.update()
            else:
                errormessage.visible = False
                errormessage.update()
    
            user = page.session.store.get('user')
    
            user['password'] = password.value

            page.session.store.set("user",user)


            page.pop_dialog()
    
            update_user(user)

    def on_next(e):
        if not username.value:
            username.helper = 'Username can not be left empty'
            username.update()
            return
        else:
            username.helper=None
            username.update()
        user = check_username(username.value)

        if not user:
            errormessage.visible = True
            errormessage.update()
            return
        else:
            errormessage.visible = False
            errormessage.update()

        page.session.store.set("user",user)

        model.title = 'reset password'
        model.content = ft.Column(
            tight=True,
            controls = [
                password,
                confirm_password,
                errormessage]
        )
        model.actions = [
                    ft.Button(
                        content='Cancel',
                        on_click=on_cancel
                    ),
                    ft.Button(
                        content='Save',
                        on_click=on_save
                        
                    )
                ]
        page.update()

  
        
    model = ft.AlertDialog(
        title='Confirm username',
        modal=True,
        content=
            ft.Column(
                tight=True,
                controls =[
                    username,
                    errormessage
                ]
        ),
        actions=[
            ft.Button(
                content='Cancel',
                on_click=on_cancel
            ),
            ft.Button(
                content='Next',
                on_click=on_next
                
            )
        ]
        
    )
    return model