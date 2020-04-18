from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
import os
from pathlib import Path
from layout import *

parent_dir = Path(__file__).parent
os.curdir = parent_dir


class MainApp(App):
    def build(self):
        return kv


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file(os.path.join(parent_dir, "layout", "layout.kv"))

if __name__ == "__main__":
    MainApp().run()
