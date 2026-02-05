import reflex as rx
from ..styles import style_navbar


def button(text:str) -> rx.Component:
    return rx.button(
        text, style=style_navbar.navbar_style
    ),

def navbar() -> rx.Component:

    return rx.container(
        
        rx.center(
            rx.hstack(                
                button("Tecnologies"),
                button("Experience"),          
                button("Proyects"),          
                button("Studies"),          
                button("More"),    
                button("Contact"),          
                rx.color_mode.button(size="4"),

            ),
        )
    )

