from sys import platform
import os


class Notifier:
    def __init__(self, title, msg):
        """
        The notifier creates a notification by executing the relevant code
        on the corresponding platform (mac and windows are currently supported)

        :param title: str, title for the notificaiton
        :param msg: str, message to display
        """
        kwargs = {}
        if platform == "linux" or platform == "linux2":
            self._notifier = None
        elif platform == "darwin":
            self._notifier = """osascript -e 'display notification "{msg}" with title "{title}"' """
        elif platform == "win32":
            from win10toast import ToastNotifier
            self._notifier = ToastNotifier()
            kwargs["duration"] = 0
        # Args for all platforms
        self.title = title
        self.msg = msg
        self.kwargs = kwargs

    @property
    def notify(self):
        """Used to access the notification method, that will be called in __call__"""
        if platform == "linux" or platform == "linux2":
            return lambda **kwargs: "Notifications unavailable on linux"  # Replace this by a method in linux
        elif platform == "darwin":
            return lambda msg, title, **kwargs: os.system(self._notifier.format(msg=msg, title=title))
        elif platform == "win32":
            return getattr(self._notifier, "show_toast")

    def __call__(self, *args, **kwargs):
        """args and kwargs need to be kept as kivy may pass additional arguments"""
        self.notify(title=self.title, msg=self.msg, **self.kwargs)
