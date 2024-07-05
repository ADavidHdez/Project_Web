import reflex as rx
from test_env.routes import Route
from test_env.components.link_button import link_button
from test_env.components.title import title
from test_env.styles.styles import Size, Spacing
from test_env.styles.styles import TextColor as TextColor
from test_env.styles.fonts import Font
import test_env.constants as const


# Links
def index_links() -> rx.Component:
    return rx.vstack(
        title("REDES"),
        link_button("LinkedIn", 
                    "Perfil Profesional",
                    "/icons/linkedin.svg",
                    const.LINKEDIN,
        ),
        link_button("Instagram", 
                    "Cuenta Fitness",
                    "/icons/instagram.svg",
                    const.INSTAGRAM_ENTRENAMIENTO_URL,
        ),
        link_button("Instagram", 
                    "Cuenta Personal",
                    "/icons/instagram.svg",
                    const.INSTAGRAM_PERSONAL_URL,                   
        ),
        link_button("Youtube", 
                    "Podcasts",
                    "/icons/youtube.svg",
                    const.PODCAST_YT_URL,            
        ),
        title("DE INTERES"),
        link_button("Galeria",
                   "Trabajos realizados",
                    "/icons/gallery.svg",
                    Route.GALLERY.value,
                    is_external=False
        ), 
        title("CONTACTO"),
        link_button("Email",
                    const.EMAIL,
                    "/icons/envelope-solid.svg", 
                    f"mailto:{const.EMAIL}",
        ),  
        width="100%",
        spacing=Spacing.DEFAULT.value,
        color=TextColor.INFOBOX.value,
        
    )