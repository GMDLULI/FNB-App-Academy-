import flet as ft
from pages.login import login_page
from pages.register import register_page



def main(page: ft.Page):

    def go_login():
        page.run_task(page.push_route, "/login")

    def route_check():
        page.views.clear()
        if page.route == '/':
            page.views.append(login_page(page))
        elif page.route == '/login':
            page.views.append(login_page(page))
        elif page.route == '/register':
            page.views.append(register_page(page, go_login))

        page.update()

    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
        top_view = page.views[-1]
        await page.push_route(top_view.route)
    page.on_route_change = route_check

    page.on_view_pop = view_pop
    route_check()
        
    


if __name__ == "__main__":
    ft.run(main)
