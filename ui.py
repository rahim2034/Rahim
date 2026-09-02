# ui.py
# শুধু UI / Button design এবং button binding এখানে থাকবে।
# Button-এর আসল কাজ actions.py-তে থাকবে।

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.metrics import dp


RED = (0.85, 0.03, 0.03, 1)
BLUE = (0.03, 0.25, 0.85, 1)
WHITE = (1, 1, 1, 1)


def create_ui(actions=None):

    main = BoxLayout(
        orientation="vertical",
        padding=dp(12),
        spacing=dp(12)
    )

    # =========================
    # TOP — 4 RED BUTTONS
    # =========================

    top = BoxLayout(
        orientation="horizontal",
        spacing=dp(8),
        size_hint_y=None,
        height=dp(85)
    )

    gen = Button(
        text="⚡\nGEN",
        font_size=dp(20),
        color=WHITE,
        background_normal="",
        background_color=RED
    )

    twofa = Button(
        text="🔐\n2FA",
        font_size=dp(20),
        color=WHITE,
        background_normal="",
        background_color=RED
    )

    uid = Button(
        text="🆔\nUID",
        font_size=dp(20),
        color=WHITE,
        background_normal="",
        background_color=RED
    )

    cookie = Button(
        text="🍪\nCOOKIE",
        font_size=dp(18),
        color=WHITE,
        background_normal="",
        background_color=RED
    )

    # =========================
    # TOP BUTTON ACTIONS
    # =========================

    if actions is not None:
        gen.bind(
            on_release=lambda x: actions.gen()
        )

        twofa.bind(
            on_release=lambda x: actions.twofa()
        )

        uid.bind(
            on_release=lambda x: actions.uid()
        )

        cookie.bind(
            on_release=lambda x: actions.cookie()
        )

    top.add_widget(gen)
    top.add_widget(twofa)
    top.add_widget(uid)
    top.add_widget(cookie)

    # =========================
    # BOTTOM — 3 BLUE BUTTONS
    # =========================

    bottom = BoxLayout(
        orientation="horizontal",
        spacing=dp(8),
        size_hint_y=None,
        height=dp(85)
    )

    set_button = Button(
        text="⚙️\nSET",
        font_size=dp(20),
        color=WHITE,
        background_normal="",
        background_color=BLUE
    )

    home = Button(
        text="🏠\nHOME",
        font_size=dp(20),
        color=WHITE,
        background_normal="",
        background_color=BLUE
    )

    exit_button = Button(
        text="⏻\nEXIT",
        font_size=dp(20),
        color=WHITE,
        background_normal="",
        background_color=BLUE
    )

    # =========================
    # BOTTOM BUTTON ACTIONS
    # =========================

    if actions is not None:
        set_button.bind(
            on_release=lambda x: actions.settings()
        )

        home.bind(
            on_release=lambda x: actions.home()
        )

        exit_button.bind(
            on_release=lambda x: actions.exit()
        )

    bottom.add_widget(set_button)
    bottom.add_widget(home)
    bottom.add_widget(exit_button)

    # =========================
    # ADD TO MAIN LAYOUT
    # =========================

    main.add_widget(top)
    main.add_widget(bottom)

    return main
