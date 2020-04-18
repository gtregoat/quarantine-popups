from sys import platform
import os


class Notifier:
    def __init__(self, *args, **kwargs):
        """kwargs must contain msg and title"""
        assert set(("msg", "title")).issubset(kwargs), "'msg' and 'title' must be provided to the notifier."
        if platform == "linux" or platform == "linux2":
            pass
        elif platform == "darwin":
            self._notifier = """osascript -e 'display notification "{msg}" with title "{title}"' """
        elif platform == "win32":
            from win10toast import ToastNotifier
            self._notifier = ToastNotifier()
            self.notification_method_name = "show_toast"
        # Args for all platforms
        self.args = args
        self.kwargs = kwargs

    @property
    def notify(self):
        if platform == "linux" or platform == "linux2":
            pass
        elif platform == "darwin":
            return lambda msg, title, **kwargs: os.system(self._notifier.format(msg=msg, title=title))
        elif platform == "win32":
            return getattr(self._notifier, self.notification_method_name)

    def __call__(self, *args, **kwargs):
        self.notify(*self.args, **self.kwargs)
