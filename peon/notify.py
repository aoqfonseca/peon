from os.path import abspath, dirname, join
import time


class Urgency(object):
    low = 0
    normal = 1
    critical = 2


def notify(app_name, title, message, image, urgency=Urgency.normal):
    try:
        notify_pynotify(app_name, title, message, image, urgency)
    except ImportError:
        notify_growl(app_name, title, message, image, urgency)
        return

def notify_growl(app_name, title, message, image, urgency=Urgency.normal):
    try:
        import Growl
    except ImportError:
        return

    path_image = abspath(join(dirname(__file__), image))
    icon = {'applicationIcon': Growl.Image.imageFromPath(path_image)}

    growl = Growl.GrowlNotifier(app_name, [app_name], **icon)
    growl.notify(app_name, title, message)

def notify_pynotify(app_name, title, message, image, urgency=Urgency.normal):
    import pynotify

    urgencies = {
        Urgency.low: pynotify.URGENCY_LOW,
        Urgency.normal: pynotify.URGENCY_NORMAL,
        Urgency.critical: pynotify.URGENCY_CRITICAL,
    }

    if pynotify.init("Nosy"):
        n = pynotify.Notification(title,
                                  message,
                                  abspath(join(dirname(__file__), image)))
        n.set_urgency(urgencies[urgency])
        n.show()
        time.sleep(2)
        n.close()
