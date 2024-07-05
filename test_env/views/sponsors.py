import reflex as rx
from test_env.components.title import title
from test_env.components.links_sponsors import link_sponsors
from test_env.styles.styles import Spacing
import test_env.constants as const

def sponsors() -> rx.Component:
    return rx.vstack(
        title("EXTRAS"),
        rx.flex(
            link_sponsors(
                "/default.gif",
                "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                "Sorpresa_Link"
            ),
            link_sponsors(
                "/default.gif",
                const.LINKEDIN,
                "LinkedIn_Link",
            ),
            spacing=Spacing.BIG.value,
            flex_direction = ["column", "row"],
        ),
        width="100%",
        align_items="center",
        spacing=Spacing.DEFAULT.value,
    ),

def opiniones() -> rx.Component:
    return rx.vstack(
        title("OPINIONES"),
        width="100%",
        align_items="center",
        spacing=Spacing.DEFAULT.value,
    )