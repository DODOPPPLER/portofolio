import reflex as rx

def tags(text: str, icon_name: str) ->rx.Component:
    return rx.hstack(
        rx.text(text),
        rx.icon(icon_name),
    ) 

def tecnologies() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.text(
                "tecnologies"
            ),
            rx.text(
                "principal"
            ),
            rx.hstack(
                tags("Python", "database"),
                rx.list.unordered(
                    rx.list_item(tags("Reflex", "database")),
                    rx.list_item(tags("FastAPI", "database")),
                    rx.list_item(tags("Django", "database")),                    
                ),
                tags("Java", "database"),
                rx.list.unordered(
                    rx.list_item(tags("Spring", "database")),
                ),
                tags("SQL", "database"),                
                rx.list.unordered(
                    rx.list_item(tags("MySql", "database")),
                    rx.list_item(tags("PostgeSQL", "database")),
                    rx.list_item(tags("SQLite", "database")),
                ),
                tags("NoSQL", "database"),                
                rx.list.unordered(
                    rx.list_item(tags("MongoDB", "database")),                    
                ),
            ),
            rx.text(
                "secondary"
            ),
            rx.hstack(
                tags("HTML", "database"),
                tags("CSS", "database"),
                tags("JS", "database"),                
            ),
        )
    )