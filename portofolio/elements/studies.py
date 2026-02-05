import reflex as rx

def studies() -> rx.Component:
    return rx.container(
        rx.text(
            "Studies"
        ),
        rx.vstack(
            rx.text("Systems Engineering – Universidad Minuto de Dios 7th semester in progress – Bogotá, Colombia"),
            rx.text("Software Development Technician – SENA Bogotá,Colombia"),
        )
    )