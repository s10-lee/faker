from os.path import dirname, abspath, join, exists, realpath, curdir
import os
import subprocess
from pynput.keyboard import Key, Controller as cone
from pynput.mouse import Button, Controller as ctwo
from random import randint
# import sys
import glob
import time

# Init
keyboard = cone()
mouse = ctwo()


def open_browser(url):
    subprocess.run(['open', url, '-F'])


def get_random(mn, mx):
    if mx and mx > mn:
        return randint(mn, mx)
    return mx


def get_source(wildcard):
    if wildcard:
        files = glob.glob(wildcard, recursive=True)
        return load_files(*files)
    return None


def load_files(*args):
    result = ''
    for f in args:
        path = join(realpath(f))
        if exists(path):
            with open(path) as fp:
                result += ''.join([l for l in fp.readlines()]) + '\n\n\n'
    return result


def press_key(char):
    delay = randint(50, 500) / 1000

    if char == '\n':
        char = Key.enter

    keyboard.press(char)
    keyboard.release(char)
    time.sleep(delay)
    return delay


def write_code(code: str):
    spent = 0
    for i, c in enumerate(code):
        spent += press_key(c)
    return round(spent, 2)


def get_console_option(shortcuts, typecast=None):
    import sys

    value = None
    length = len(sys.argv)

    # TODO: WTF ?
    # sys_args = []
    # for a in tuple(sys.argv):
    #     sys_args.append(a)

    if length:
        for index, argument in enumerate(sys.argv):
            if argument in shortcuts and length > index + 1:
                value = sys.argv[index + 1]
                if typecast:
                    return typecast(value)

    return value


def command_tab():
    with keyboard.pressed(Key.cmd_l):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)


# def mouse_y(v, step, start, end, interval):
#     while True:
#         v += step
#         if start < v < end:
#             time.sleep(interval)
#             mouse.move(0, step)
#         else:
#             break
#     return v


def mouse_move(val, step, start, end, interval):
    while True:
        val += step
        if start <= val <= end:
            time.sleep(interval)
            mouse.move(step, 0)
        else:
            break
    return val


def fake_mouse(limit=5):
    x, y = 400, 400
    itr = .002
    mouse.position = (400, 400)
    time.sleep(2)

    for _ in range(limit):
        y = mouse_move(y, 1, 400, 800, itr)
        x = mouse_move(x, 1, 600, 900, itr)
        y = mouse_move(y, -1, 400, 800, itr)
        x = mouse_move(x, -1, 600, 900, itr)


if __name__ == '__main__':
    fake_mouse(5)

