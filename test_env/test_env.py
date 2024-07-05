import reflex as rx

from test_env.pages.index import index
from test_env.pages.gallery import gallery
import test_env.styles.styles as styles
import test_env.constants as const
from rxconfig import config




app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets= [
        "/fonts/myfont.css",  # This path is relative to assets/
        "https://fonts.googleapis.com/css2?family=Comfortaa:wght@300..700&display=swap",
        "https://fonts.googleapis.com/css2?family=Comfortaa:wght@300..700&family=Dosis:wght@200..800&display=swap"  
    ],
    head_components=[
        rx.script(src=f"https://www.googletagmanager.com/gtag/js?id={const.G_TAG}"),
        rx.script(
            f"""
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments);}}
            gtag('js', new Date());
            gtag('config', '{const.G_TAG}');
            """
        ),
    ],
)

