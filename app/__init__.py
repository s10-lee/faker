from utils import show_app, wait, open_in_app, write_text, command, close_app, alert, press_key
import time
from multiprocessing import Process


def start_task(func, *args, **kwargs):
    p = Process(target=func, args=args, kwargs=kwargs)
    p.start()


filename = '../_source/index.js'


def run():
    schedule = [

        (open_in_app, 'Firefox', 'https://inviqa.com/blog/eav-data-model'),

        (wait, 10),

        (alert, 'Scroll Down'),
        (press_key, ' '),

        (wait, 5),

        (alert, 'Touch file index.js'),
        (command, 'touch', filename),

        (open_in_app, 'Visual Studio Code', filename),

        (wait, 10),

        (write_text, '// Мне бы очень хотелось сегодня получить результат и уже наканец начать разработку \n', 8),

        (wait, 10),

        (close_app, 'Firefox'),

        (alert, 'Remove index.js'),
        (command, 'rm', filename),

        (wait, 10),

        (show_app, 'PyCharm'),

        (wait, 10),

        (close_app, 'Visual Studio Code'),

        (alert, 'DONE !')
    ]


    for (f, *params) in schedule:
        f(*params)


# run()
