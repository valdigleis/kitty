from kitty.fast_data_types import Screen
from kitty.tab_bar import DrawData, ExtraData, as_rgb


def draw_tab(
    draw_data: DrawData,
    screen: Screen,
    tab,
    before,
    max_title_length,
    index,
    is_last,
    extra_data: ExtraData,
):

    active_bg = as_rgb(0x606060)
    inactive_bg = as_rgb(0x303030)

    bg = active_bg if tab.is_active else inactive_bg

    # Fundo da aba
    screen.cursor.bg = bg
    screen.cursor.fg = as_rgb(0xffffff)

    title = f" {tab.title} "
    screen.draw(title)

    # Separador degradê
    shades = [
        (0x505050, "░"),
        (0x404040, "▒"),
        (0x383838, "▓"),
        (0x303030, "█"),
    ]

    for color, char in shades:
        screen.cursor.bg = as_rgb(color)
        screen.cursor.fg = as_rgb(color)
        screen.draw(char)
