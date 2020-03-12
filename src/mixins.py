from src.console import BaseConsole
from random import randint
import sys


def h1(text):
    BaseConsole.write(text, bold=True, color='white')


def nl(times=0):
    print(BaseConsole.CRLF * times)


def echo(text, **kwargs):
    BaseConsole.write(text, **kwargs)


def info(text, **kwargs):
    echo(text, color='cyan', **kwargs)


def success(text, **kwargs):
    echo(text, color='green', **kwargs)


def error(text, **kwargs):
    echo(text, color='red', **kwargs)


def confirm(text, **kwargs):
    return BaseConsole.read(text, var_type=bool, **kwargs)


def ask(text, **kwargs):
    return BaseConsole.read(text, var_type=int, **kwargs)


def get_offset(min, max):
    if max:
        return randint(min, max)
    return min


def get_args(**kwargs):

    timeout = kwargs.get('timeout', 10)

    if len(sys.argv) > 1:
        for index, argument in enumerate(sys.argv):
            if argument in ['--timeout', '--time', '-t'] and len(sys.argv) > index + 1:
                timeout = int(sys.argv[index + 1])

            if argument in ['--interval', '--int', '-i'] and len(sys.argv) > index + 1:
                interval = int(sys.argv[index + 1])

    return timeout
