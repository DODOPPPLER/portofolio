import reflex as rx
from ..styles import general_styles
from ..styles import style_tecnologies

def tags(text: str, icon_name: str) ->rx.Component:
    return rx.hstack(
        rx.image(
            src=icon_name,
            style=style_tecnologies.img_style
            ),
        rx.text(text),
        style=style_tecnologies.tag_style
    ) 

def tecnologies() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.text(
                "Tecnologies",
                style=style_tecnologies.title_style,
                
            ),
            rx.spacer(height="9em"),
            rx.text(
                "Principal",
                style=style_tecnologies.subtitle_style,
            ),
            rx.hstack(
                tags("Python", "/python.png"),
                rx.vstack(
                    tags("Reflex", "/database"),
                    tags("FastAPI", "database"),
                    tags("Django", "/django.png"),
                    margin_right="1.5em", 
                ),

                tags("Java", "/java.png"),
                rx.vstack(
                    tags("Spring", "/spring-boot.png"),
                ),
                margin_bottom="1.5em",            
            ),
            rx.hstack(
                tags("SQL", "/sql-server.png"),   
                rx.vstack(
                    tags("MySql", "/database.png"),
                    tags("PostgeSQL", "/database(1).png"),
                    tags("SQLite", "database"),
                    margin_right="1.5em", 
                ),                  
                tags("NoSQL", "/unstructured-data.png"),
                rx.vstack(
                    tags("MongoDB", "database"),
                ),                              
            ),           
            rx.text(
                "Secondary",
                style=style_tecnologies.subtitle_style,
            ),
            rx.hstack(
                tags("HTML", "/html-5.png"),
                tags("CSS", "/css-3.png"),
                tags("JS", "/java-script.png"),                
            ),
            align="center",
        )
    )