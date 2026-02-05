import reflex as rx

def more() -> rx.Component:
    return rx.container(
        rx.text(
            "More"
        )
    )