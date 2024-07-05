import reflex as rx
import datetime
from test_env.styles.colours import Color, TextColor
from test_env.components.link_icon import link_icon
from test_env.components.info_text import info_text
from test_env.styles.styles import Size, Spacing
from test_env.styles.fonts import Font
import test_env.constants as const
from test_env.styles.fonts import FontWeight


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Ángel David",
                size="8",
                padding="2px",
                radius="full",
                border="4px",
                color=Color.BACKGROUND.value,
                bg=TextColor.HEADER.value,
                src="/perfil2.png",
            ),
            rx.vstack(
                rx.heading(
                    "Ángel David Hernández",
                    size=Spacing.BIG.value,
                ),
                rx.link(
                    rx.text(
                        "@david421",
                        margin_top=Size.ZER0.value,
                        color = "#000000",
                        ),
                    href=const.INSTAGRAM_PERSONAL_URL,
                    is_external=True,       
                ),
                rx.hstack(
                    link_icon(
                        "/icons/whatsapp.svg",
                        const.WHATSAPP_GROUP,
                        alt="Whatssap"
                    ),
                    link_icon(
                        "/icons/linkedin.svg",
                        const.LINKEDIN,
                        alt="LinkedIn"
                    ),
                    link_icon(
                        "/icons/instagram.svg",
                        const.INSTAGRAM_PERSONAL_URL,
                        alt="Instagram_Personal",
                    ),
                    link_icon(
                        "/icons/instagram.svg",
                        const.INSTAGRAM_ENTRENAMIENTO_URL,
                        alt="Instagram_Entrenamiento"
                    ),
                    link_icon(
                        "/icons/spotify.svg",
                        const.SPOTIFY_PLAYLIST_URL,
                        alt="Spotify"
                    ),
                    spacing=Spacing.LARGE.value,
                    padding_top=Size.SMALL.value,
                ),
                spacing=Spacing.ZER0.value,
                align_items="start"
            ),
            align="end",
            spacing=Spacing.DEFAULT.value,
        ),
        rx.vstack(
            rx.flex(
                info_text(
                    f"{experience()}+",
                    "Años Entrenando"
                ),
                rx.chakra.spacer(),
                info_text(
                    "4+", "Años de Estudios"
                ),
                rx.chakra.spacer(),
                info_text(
                    "3+", "Proyectos Personales"
                ),
                width="100%"
            ),
            width="100%"
        ),
        rx.text(
            f"""Soy graduado como técnico en sistemas eléctricos y automatizados
            así como técnico en robotica industrial. Llevo varios años en el mundo del
            entrenamiento personal y el fitness. Me gusta realizar pequeños proyectos
            personales que me motivan cada día, aquí abajo dejo los enlaces por si te 
            interesan""",
            color=Color.PRIMARY.value,
            font_size=Size.DEFAULT.value,
            font_family= Font.TITULO.value,
            font_weight= FontWeight.MEDIUM.value,
        ),
        width="100%",
        spacing=Spacing.BIG.value,
        align_items="start"
    )


def experience() -> int:
    return datetime.date.today().year - 2018