from src.console import BaseConsole

echo = BaseConsole.write


def echo_nl(*args, indent=1, **kwargs):
    indent = int(indent)
    kwargs['end'] = None
    crlf = abs(indent) * '\n'
    if indent > 0:
        arguments = *args, abs(indent) * '\n'
    else:
        kwargs['end'] = ''
        arguments = abs(indent) * '\n', *args
    echo(*arguments, **kwargs)


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
    return BaseConsole.read(text, var_type=bool, **kwargs)


def ask(text, **kwargs):
    return BaseConsole.read(text, var_type=int, **kwargs)
