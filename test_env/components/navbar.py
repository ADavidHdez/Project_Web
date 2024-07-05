import reflex as rx
from test_env.routes import Route
from test_env.styles.styles import Size
from test_env.styles.colours import TextColor as TextColor
from test_env.styles.colours import Color as Color
import test_env.styles.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text("David", as_="span", color=Color.PRIMARY.value),
                rx.text("Hdez", as_="span", color=Color.SECONDARY.value),
                style= styles.navbar_title_style,
                #width ="50%",
            ),
            href=Route.INDEX.value
        ),
        #padding="5em",
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
    )