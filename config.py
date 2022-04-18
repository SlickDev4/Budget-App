from kivy.config import Config
from kivy.core.window import Window


def config():
    Config.set('graphics', 'resizable', False)
    Config.write()
    Window.size = (1330, 675)
    Window.top = 40
    Window.left = 20
    Window.resize = False


config()
