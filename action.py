# actions.py
# শুধু Button-এর কাজ থাকবে।
# UI/design এখানে থাকবে না।

from kivy.app import App


class Actions:

    # =========================
    # TOP BUTTONS
    # =========================

    def gen(self):
        print("GEN button pressed")

    def twofa(self):
        print("2FA button pressed")

    def uid(self):
        print("UID button pressed")

    def cookie(self):
        print("COOKIE button pressed")

    # =========================
    # BOTTOM BUTTONS
    # =========================

    def settings(self):
        print("SET button pressed")

    def home(self):
        print("HOME button pressed")

    def exit(self):
        app = App.get_running_app()

        if app:
            app.stop()
