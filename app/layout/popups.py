from kivy.uix.popup import Popup


class ShowPopup:
    def __init__(self, pop_class, *args, **kwargs):
        show = pop_class(*args, **kwargs)
        self.popup_window = Popup(title="Popup Window",
                                  content=show,
                                  size_hint=(None, None),
                                  size=(400, 400))

    def __call__(self, *args, **kwargs):
        self.popup_window.open()

    def dismiss(self):
        self.popup_window.dismiss()
