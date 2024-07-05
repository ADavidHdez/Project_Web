import reflex as rx
import test_env.styles.styles as styles
from test_env.styles.styles import Spacing
from test_env.styles.colours import Color as Color

def link_sponsors(imagen:str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=imagen,
            height="8.5em",
            width="auto",   #Que la imagen guarde la proporción
            alt=alt
        ),
        href=url,
        is_external=True
    )