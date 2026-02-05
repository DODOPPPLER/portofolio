import reflex as rx

from ..styles import style_profile
from ..styles import general_styles

class MailState(rx.State):
    show_send : bool = False
    text: str = "Show Mail"
    color: str = general_styles.color_primary
    cursor: str = "pointer"

    @rx.event
    def change_to_mail(self):
        if self.text == "Show Mail":
            self.show_send = True
            self.text = "morenokevinfelipe@gmail.com"
            self.color = general_styles.border_color
            self.cursor = "default"
        else:
            self.text = "Show Mail"
            self.show_send = False
            self.color = general_styles.color_primary
            self.cursor = "pointer"

def mail_show() ->rx.Component:
    return rx.hstack(
        rx.link(
            rx.button(
                rx.icon("mail"), 
                MailState.text,
                style=style_profile.buttons_style,
                bg_color = MailState.color,
                cursor = MailState.cursor,
            ),
            on_click=MailState.change_to_mail(),
        ),
        rx.cond(
            MailState.show_send,
            rx.link(
                rx.button(
                    rx.icon("mail"), 
                    "Send a mail",
                    style=style_profile.buttons_style,
                    ),
                href="mailto:kevin@example.com",
                is_external=True,                           
            ),
        ),    
    )

def button_with_icon(icon_name: str, text: str, link: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(icon_name), 
            text,
            style=style_profile.buttons_style 
        ),
        href=link,
        is_external=True,
               
    )

def contact() -> rx.Component:
    return rx.container(
        rx.text(
            "Contact",
            rx.hstack(
                button_with_icon("github","Github","https://github.com/DODOPPPLER"),                          
                button_with_icon("linkedin", "Linkedin","https://www.linkedin.com/in/kevin-felipe-moreno-ramirez-863b59144/"),
                rx.link(
                    rx.button(
                        rx.icon("download"), 
                        "CV",
                        style=style_profile.buttons_style
                        ),
                    href=rx.asset("CV_Kevin_Moreno_ES.pdf"),
                    is_external=True,      
                ),
                mail_show(),                
                style=style_profile.hstack_style,                 
            ),
        )
    )