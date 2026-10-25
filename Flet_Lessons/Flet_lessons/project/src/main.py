import flet as ft
from pages.home import home_page
from pages.greet import greet_page


def main(page: ft.Page):
    def route_check():
            page.views.clear()
            if page.route == '/':
                page.views.append(home_page(page))
            elif page.route == '/home':
                page.views.append(home_page(page))
            elif page.route == '/greeting':
                username = page.session.store.get("username") or "Guest"
                page.views.append(greet_page(page,username))
    
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
