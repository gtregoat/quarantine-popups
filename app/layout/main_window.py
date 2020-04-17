from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from .exercise import show_exercise_popup, Exercise
from .popups import ShowPopup
from kivy.lang import Builder


class MainWindow(Screen):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.init = True

    def on_enter(self):
        self.set_timer()

    def show_exercise_popup(self, *args):
        show_exercise_popup()

    def set_timer(self):
        value = self.ids['time_to_reminder'].text if "time_to_reminder" in self.ids else 30
        try:
            value = float(value) * 60
        except ValueError:
            show_error_popup()
            return
        Clock.unschedule(self.show_exercise_popup)
        Clock.schedule_interval(self.show_exercise_popup, value)
        if self.init:
            self.init = False
        else:
            show_time_changed_popup()



Builder.load_string("""

<Error>:
    Label:
        text: "The time set needs to be numeric!"
        size_hint: 0.6, 0.2
        pos_hint: {"x":0.2, "top":1}

    Button:
        text: "Close"
        size_hint: 0.8, 0.2
        pos_hint: {"x": 0.1, "y": 0.1}
        on_release:  root.dismiss()
        
        
<TimeChanged>
    Label:
        text: "Successfully changed time between exercises!"
        size_hint: 0.6, 0.2
        pos_hint: {"x":0.2, "top":1}

    Button:
        text: "Close"
        size_hint: 0.8, 0.2
        pos_hint: {"x": 0.1, "y": 0.1}
        on_release:  root.dismiss()
""")


class Error(FloatLayout):
    def __init__(self, **kwargs):
        super(Error, self).__init__(**kwargs)

    def dismiss(self):
        show_error_popup.dismiss()


class TimeChanged(FloatLayout):
    def __init__(self, **kwargs):
        super(TimeChanged, self).__init__(**kwargs)

    def dismiss(self):
        show_time_changed_popup.dismiss()


show_error_popup = ShowPopup(Error)
show_time_changed_popup = ShowPopup(TimeChanged)
