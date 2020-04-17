from sys import platform


class Notifier:
    def __init__(self, *args, **kwargs):
        if platform == "linux" or platform == "linux2":
            pass
        elif platform == "darwin":
            # OS X
            pass
        elif platform == "win32":
            from win10toast import ToastNotifier
            self._notifier = ToastNotifier()
            self.notification_method_name = "show_toast"
            self.args = args
            self.kwargs = kwargs

    @property
    def notify(self):
        if platform == "linux" or platform == "linux2":
            pass
        elif platform == "darwin":
            # OS X
            pass
        elif platform == "win32":
            return getattr(self._notifier, self.notification_method_name)

    def __call__(self, *args, **kwargs):
        self.notify(*self.args, **self.kwargs)
