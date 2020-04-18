from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from .exercise import show_exercise_popup, Exercise
from .popups import ShowPopup
from kivy.lang import Builder
from .desktop_notifications import Notifier


class MainWindow(Screen):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.init = True
        self.seconds = 0
        self.remaining_seconds = -1

    def on_enter(self):
        self.set_timer()

    def show_exercise_popup(self, *args):
        show_exercise_popup()

    def set_time(self, minutes):
        self.seconds = int(minutes * 60)
        self.remaining_seconds = self.seconds
        Clock.unschedule(self.show_exercise_popup)
        Clock.unschedule(self.update_timer)
        Clock.schedule_interval(self.show_exercise_popup, self.seconds)
        Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, arg):
        self.remaining_seconds -= 1
        if self.remaining_seconds < 0:
            self.remaining_seconds = self.seconds - 1  # One second would have already passed
        hours = int(max(self.remaining_seconds // 3600, 0))
        minutes = int(max(self.remaining_seconds // 60, 0))
        seconds = int(max(self.remaining_seconds - hours * 3600 - minutes * 60, 0))
        self.ids['timer_text'].text = "time to next exercises: \n{:0>2}:{:0>2}:{:0>2}".format(hours, minutes, seconds)

    def set_timer(self):
        value = self.ids['time_to_reminder'].text if "time_to_reminder" in self.ids else 30
        try:
            value = float(value)
        except ValueError:
            show_error_popup()
            return
        self.set_time(value)
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


show_error_popup = ShowPopup(Error, Notifier(title="Quarantine app", msg="Error changing timer"))
show_time_changed_popup = ShowPopup(TimeChanged, Notifier(title="Quarantine app", msg="Timer changed!"))
