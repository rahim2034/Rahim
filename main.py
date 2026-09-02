# main.py
# Main entry point
# UI + Actions + Shield একসাথে চালাবে

from kivy.app import App

from ui import create_ui
from actions import Actions
from shield import shield_enabled


class MyApp(App):

    def build(self):

        # Shield চালু আছে কিনা পরীক্ষা
        if not shield_enabled():
            raise RuntimeError("Privacy Shield is disabled")

        # Button actions
        actions = Actions()

        # UI তৈরি
        return create_ui(actions)


if __name__ == "__main__":
    MyApp().run()
