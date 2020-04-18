from kivy.uix.popup import Popup


class ShowPopup:
    def __init__(self, pop_class, notifier, *args, **kwargs):
        self.notifier = notifier
        self.pop_class = pop_class
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        self.notifier(*args, **kwargs)
        show = self.pop_class(*self.args, **self.kwargs)
        self.popup_window = Popup(title="Popup Window",
                                  content=show,
                                  size_hint=(None, None),
                                  size=(400, 400))
        self.popup_window.open()

    def dismiss(self):
        self.popup_window.dismiss()
