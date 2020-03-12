from os.path import dirname, abspath, join, exists, realpath, curdir
import os
from pynput.keyboard import Key, Controller
from random import randint
import sys
from glob import glob
import time
keyboard = Controller()


def get_random(mn, mx):
    if mx and mx > mn:
        return randint(mn, mx)
    return mx


def get_source(wildcard):
    if wildcard:
        files = glob(wildcard, recursive=True)
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


def get_console_option(shortcuts, typecast=None, default=None):
    value = default
    length = len(sys.argv)
    if isinstance(shortcuts, str):
        shortcuts = [shortcuts]

    if length:
        for index, argument in enumerate(sys.argv):
            if argument in shortcuts and length > index + 1:
                value = sys.argv[index + 1]

                if typecast:
                    return typecast(value)

    return value
