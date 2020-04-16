from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
import os
from pathlib import Path
from layout import *


class MainApp(App):
    def build(self):
        return kv


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file(os.path.join(Path(__file__).parent, "layout", "layout.kv"))

if __name__ == "__main__":
    MainApp().run()
