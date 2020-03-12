from src.console import BaseConsole

echo = BaseConsole.write


# TODO: Move crappy header here !
def print_greetings():
    pass


def h1(text):
    BaseConsole.write(text, bold=True, color='white')


def nl(times=0):
    print(BaseConsole.CRLF * times)


def info(text, **kwargs):
    echo(text, color='cyan', **kwargs)


def success(text, **kwargs):
    echo(text, color='green', **kwargs)


def error(text, **kwargs):
    echo(text, color='red', **kwargs)


def confirm(text, **kwargs):
    result = BaseConsole.read(text, var_type=bool, **kwargs)
    return result


def ask(text, **kwargs):
    return BaseConsole.read(text, var_type=int, **kwargs)
