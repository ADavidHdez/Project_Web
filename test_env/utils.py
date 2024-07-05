import reflex as rx

# Comun

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

preview = "assets/desenfoque.jpg"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@_David421"}
]
    
# Indexs

index_title = "DavidHdez | Página Web"
index_description = "Técnico en sistemas eléctricos y automatizados"

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]

index_meta.extend(_meta)

# Gallery

gallery_title = "DavidHdez | Gallery"
gallery_description = "Trabajos Técnicos Realizados"

gallery_meta = [
    {"name": "og:title", "content": gallery_title},
    {"name": "og:description", "content": gallery_description},
]

gallery_meta.extend(_meta)
