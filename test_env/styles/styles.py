import reflex as rx
from enum import Enum
from .colours import Color as Color
from .colours import TextColor as TextColor
from test_env.styles.fonts import Font
from test_env.styles.fonts import FontWeight

#Constants
MAX_WIDTH="560px"

#Sizes
class Size(Enum):
    ZER0 = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
    ULTRA_BIG = "5em"

class Spacing(Enum):
    ZER0 = "0"
    VERY_SMALL = "1"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"

#Fonts
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Dosis:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
    "https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap",
]


#Styles
BASE_STYLE = {                                      #ESTILOS GENERALES DE LA PÁGINA
    "font_family": Font.TITULO.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    "background_image" :"linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
    rx.heading: {
        "color": TextColor.HEADER.value,
        "font_family": Font.TITULO.value,
        "font_weight" : FontWeight.MEDIUM.value
    },
    rx.button: {
        "width": "100%",      #COMPONENTES CSS
        "height":"100%",
        "padding":Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.INFOBOX.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "--cursor-button":"pointer",
        "_hover": {
            "background_color": Color.BOX.value
        }
    },
    rx.link: {
        "text_decoration":"none",
        "_hover": {}
    }
}

navbar_title_style = dict(
    font_family= Font.LOGO.value,
    font_weight = FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value
)  
title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    font_size=Size.LARGE.value
)
buttom_titles_style = dict(
    font_size=Size.DEFAULT.value,
    color=TextColor.INFOBOX.value,
    font_family= Font.TITULO.value,
    font_weight= FontWeight.LIGHT.value,
)

buttom_body_style = dict(
    font_size=Size.MEDIUM.value,
    color=TextColor.INFOBOX.value
)
text_footer_body_style = dict(
    font_size=Size.LARGE.value,
    color=TextColor.INFOBOX.value,
    font_family= Font.LOGO.value,
)
