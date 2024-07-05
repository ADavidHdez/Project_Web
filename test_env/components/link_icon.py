import reflex as rx
import test_env.styles.styles as styles
from test_env.styles.colours import Color as Color
from test_env.styles.styles import Size as Size


def link_icon(image: str, url:str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=Size.DEFAULT.value,
            alt=alt
        ),
        href=url,
        is_external=True,
        color = Color.SECONDARY.value,
    )