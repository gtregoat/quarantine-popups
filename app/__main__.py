from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
import os
from pathlib import Path
from .layout import *


class MainApp(App):
    def build(self):
        return kv


class WindowManager(ScreenManager):
    pass


parent_dir = Path(__file__).parent
os.chdir(parent_dir)
kv = Builder.load_file(os.path.join(parent_dir, "layout", "layout.kv"))


def run():
    MainApp().run()

