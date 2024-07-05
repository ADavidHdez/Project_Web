import reflex as rx

import test_env.constants as const
from test_env.components.date_year import get_year
from test_env.styles.styles import Size, Spacing
from test_env.styles.colours import TextColor, Color
from test_env.styles.fonts import FontWeight

year = get_year()

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/favicon.png",
            height=Size.ULTRA_BIG.value,
            weight="auto",
            alt="Logotipo de la Web | David"
        ),
        rx.link(
            f"© 2023{year} ANGEL DAVID.",
            as_="b",
            href="https://www.instagram.com/_david421_/",
            is_external=True,
            font_size=Size.DEFAULT.value,
            color=Color.PRIMARY.value,
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/github.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value
                ),
            rx.text(
                "ELECTRICIAN AND TECHNOLOGY FROM TENERIFE TO THE WORLD",
                as_="b", 
                font_size=Size.DEFAULT.value,
                font_weight= FontWeight.LIGHT.value,
                margin_top=Size.ZER0.value,
                align="center"
                ),
                color=TextColor.FOOTER.value,
            ),
            href=const.REPO_URL,
            is_external=True
        ),
        align_items ="center",
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.VERY_BIG.value,
        spacing=Spacing.ZER0.value,
        color=TextColor.FOOTER.value,
        width="100%"
    )
        
