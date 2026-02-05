import reflex as rx

def elements(title:str, site:str, date:str, description:list[str]) -> rx.Component:
    return rx.vstack(
        rx.text(title),
        rx.text(site),
        rx.text(date),
        rx.list.unordered(
            *[rx.list_item(desc) for desc in description]
        )
    )

def experience() -> rx.Component:
    return rx.container(
        rx.text(
            "Experience"
        ),
        elements(
            "Maintenance Technician and Developer",
            "Alimentos Cárnicos – Bogotá",
            "September 2024 – September 2025",
            [
                "Performed on-site maintenance and technical support for printers, computer equipment, and structured cabling",
                "Diagnosed and resolved structured cabling failures and connectivity issues.",            
                "Developed and led internal projects using JavaScript and Google Apps Script to automate processes and optimize work time."                
            ]
        ),
        elements(
            "Front-End Developer",
            "SENA – Gustavo Campos Guevara Institution",
            "June 2018 – November 2020",
            [
                "Designed and implemented an attendance and excuse management system using HTML and CSS.",
                "Developed intuitive and responsive interfaces for multiple devices.",
                "Improved school attendance tracking and registration, increasing administrative efficiency."
            ]
        )
    )