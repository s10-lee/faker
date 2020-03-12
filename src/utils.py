from os.path import dirname, abspath, join, exists, realpath, curdir
import os
from pynput.keyboard import Key, Controller
from random import randint
import sys
from glob import glob

keyboard = Controller()


def get_random(mn, mx):
    if mx and mx > mn:
        return randint(mn, mx)
    return mx


def get_source_files(wildcard):
    if wildcard:
        files = glob(wildcard, recursive=True)
        return files
    return None


def get_source_from_files(*args):
    result = ''
    for f in args:
        path = join(realpath(f))
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
    value = None
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
