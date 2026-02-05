import reflex as rx

from rxconfig import config
from .elements.navbar import navbar
from .elements.profile import profile
from .elements.tecnologies import tecnologies
from .elements.experience import experience
from .elements.proyects import proyects
from .elements.studies import studies
from .elements.more import more
from .elements.contact import contact



class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        navbar(),
        rx.spacer(height="3em"),
        profile(),
        tecnologies(),
        proyects(),
        experience(),
        studies(),
        more(),
        contact(),        

        background_color="#272727",
        max_width="85vw",
        margin="auto",
        
    )


app = rx.App()
app.add_page(index)
