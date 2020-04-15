from random import randint
import time
import subprocess
from pynput import keyboard, mouse


class Application:

    def __init__(self, name, **kwargs):
        self.name = name

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.name


class Event:
    """
        Источники собыйтий:
        - События Мыши      двигать курсор
        - Клавиатуры        нажимать кнопки
        - Системные         открыть / закрыть приложение
    """

    kc = keyboard.Controller()
    mc = mouse.Controller()


    def __call__(self, *args, **kwargs):
        print(args, kwargs)


    @classmethod
    def key_press(cls, char, delay):

        if char == '\n':
            char = keyboard.Key.enter

        cls.kc.press(char)
        cls.kc.release(char)

        time.sleep(delay)
        return delay

    @classmethod
    def mouse_move(cls, x, y):
        cls.mc.move(x, y)


    @classmethod
    def open_app(cls, name):
        command = ['osascript', '-e', f'tell application "{name}" to activate']
        process = subprocess.run(command, stdout=subprocess.PIPE)
        result = [n.strip() for n in process.stdout.decode().split(',')]
        return result



class Task:
    def __init__(self, event, *args, **kwargs):
        self.event = event
        self.ag = args
        self.kw = kwargs


    def __call__(self):
        return self.event(*self.ag, **self.kw)


