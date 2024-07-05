import reflex as rx
import test_env.styles.styles as styles
from test_env.styles.styles import Size, Spacing

def link_button(title: str, body: str, image: str, url: str, is_external=True) -> rx.Component:
    return rx.link(
        rx.button(
           rx.hstack(
               rx.image(
                   src=image,
                   width=Size.LARGE.value,
                   height=Size.LARGE.value,
                   margin=Size.MEDIUM.value,
                   alt=title
               ),
               rx.vstack(
                  rx.text(title, size=Spacing.SMALL.value,  style=styles.buttom_titles_style),
                  rx.text(body, size=Spacing.VERY_SMALL.value, style=styles.buttom_body_style),
                  align_items="start",
                  spacing=Spacing.VERY_SMALL.value,
                  padding_y=Size.SMALL.value,
                  padding_right=Size.SMALL.value,
               ),
               align="center",
               width="100%"
           ) 
        ),
        href=url,
        is_external=is_external,
        width="100%",
        text_decoration="none"
    )