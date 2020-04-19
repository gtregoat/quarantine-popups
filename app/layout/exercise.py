from kivy.uix.floatlayout import FloatLayout
from .popups import ShowPopup
from kivy.lang import Builder
from .desktop_notifications import Notifier
import os
from random import randint
from pathlib import Path
import os

# checking .gif instead of splitting
# in case other files are there and there are no "."
parent_dir = Path(__file__).parent
GIFS = [i for i in os.listdir(os.path.join(parent_dir, "resources")) if ".gif" in i or ".png" in i]


Builder.load_string("""

<Exercise>:

    Image:
        id: img
        center: self.parent.center
        allow_stretch: True
        size_hint_x: 0.6
    
    Label:
        id: exercise
        halign: 'center'
        size_hint: 0.6, 0.2
        pos_hint: {"x":0.2, "top":1}
        
    Button:
        text: "Close"
        size_hint: 0.8, 0.2
        pos_hint: {"x": 0.1, "y": 0}
        on_release:  root.dismiss()
""")


class Exercise(FloatLayout):
    def __init__(self, **kwargs):
        super(Exercise, self).__init__(**kwargs)
        exercise = GIFS[randint(0, len(GIFS) - 1)]
        self.ids['img'].source = os.path.join("layout", "resources", exercise)
        self.ids['exercise'].text = f"Time to exercise! \n{exercise.split('.')[0]}"

    def dismiss(self):
        show_exercise_popup.dismiss()


show_exercise_popup = ShowPopup(Exercise, Notifier(title="Quarantine app",
                                                   msg="Time to exercise! Check the quarantine app for ideas."))
