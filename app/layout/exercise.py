from kivy.uix.floatlayout import FloatLayout
from .popups import ShowPopup
from kivy.lang import Builder
from .desktop_notifications import Notifier

Builder.load_string("""

<Exercise>:
    Label:
        text: "Time for exercise!"
        size_hint: 0.6, 0.2
        pos_hint: {"x":0.2, "top":1}

    Button:
        text: "Close"
        size_hint: 0.8, 0.2
        pos_hint: {"x": 0.1, "y": 0.1}
        on_release:  root.dismiss()
""")


class Exercise(FloatLayout):
    def __init__(self, **kwargs):
        super(Exercise, self).__init__(**kwargs)

    def dismiss(self):
        show_exercise_popup.dismiss()


show_exercise_popup = ShowPopup(Exercise, Notifier(title="Quarantine app",
                                                   msg="Time to exercise! Check the quarantine app for ideas."))
