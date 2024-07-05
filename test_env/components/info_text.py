import reflex as rx
from test_env.styles.styles import Size, Spacing
from test_env.styles.colours import TextColor as TextColor
from test_env.styles.colours import Color as Color

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            as_="span",
            font_weight="bold",
            color=Color.PRIMARY.value,
            size=Spacing.DEFAULT.value,
        ),
        f" {body}",
        font_size=Size.DEFAULT.value,
        color=TextColor.BODY.value,
    )
