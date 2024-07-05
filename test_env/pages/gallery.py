import reflex as rx
import test_env.utils as utils
from test_env.routes import Route
from test_env.components.navbar import navbar
from test_env.components.footer import footer
from test_env.views.header import header
from test_env.views.index_links import index_links
from test_env.views.sponsors import sponsors
import test_env.styles.styles as styles
from test_env.styles.styles import Size

@rx.page(
    route=Route.GALLERY.value,
    title=utils.gallery_title,
    description=utils.gallery_description,
    image=utils.preview,
    meta=utils.gallery_meta
)
def gallery() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                index_links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )
