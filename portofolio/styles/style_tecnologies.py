from . import general_styles as gs
tecnologies_style = {
    "bg_color": gs.color_primary,
    "font_size": gs.font_medium,
    "color": "white",   
    "padding": gs.padding_standard,
    "border-style": "Solid",
    "border-color": gs.border_color,
    "border_radius": "10em",
    "cursor": "pointer",
    "width": "7em",
}
title_style = {
    "font_size": gs.font_large,
    "font_weight": "bold",
    "padding_bottom": "0.5em",
    "border_bottom": f"0.2em solid {gs.border_color}",
    "margin_bottom": "0.5em",
    "min_width": "100%",
    "text_align": "center",
}

subtitle_style = {
    "font_size": gs.font_medium,
    "font_weight": "bold",
    "padding_bottom": "0.5em",
    "margin_bottom": "0.4em",
    "border_bottom": f"0.18em solid {gs.border_color}",
    "min_width": "80%",
    "text_align": "center",
}

tag_style ={
    "max_height": "2.2em",

    "bg_color": gs.color_primary,
    "font_size": gs.font_small,
    "color": "white",
    "padding": gs.padding_standard,
    "border_radius": "10em",
    "cursor": "pointer",
    "min_width": "9em",
    "max_width": "9em",
    "align_items":"center",
    "justify_content":"center",
}
img_style ={
    "max_height": "1.8em",
}