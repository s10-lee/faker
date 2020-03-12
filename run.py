from pynput.keyboard import Key, Controller
from src.mixins import success, info, echo, ask, confirm, get_offset, nl, h1
import time


def run():
    keyboard = Controller()

    nl(1)
    h1('* * * * * * * * * *')
    h1('*                 *')
    echo('*  ', bold=True, color='white', end='')
    echo('^___^ ', bold=True, color='purple', end='', blink=True)
    echo(' *', bold=True, color='white')
    h1('*                 *')
    echo('*  ', bold=True, color='white', end='')
    echo('Faker ', bold=True, color='white', end='')
    echo(' *', bold=True, color='white')
    h1('*                 *')
    h1('* * * * * * * * * *')
    nl(1)

    # User input
    timeout = ask('Total time in minutes ?', default=10, greater=5) * 60
    echo(f'{timeout // 60} min')
    nl()

    minimum = ask('Minimum interval in seconds', greater=5, default=12)
    echo(f'{minimum} sec')
    nl()

    maximum = ask('Maximum interval, for random offset', greater=minimum + 1, default=20)
    if maximum:
        echo(f'{maximum} sec')

    nl(1)
    echo('START', bold=True, color='cyan')
    nl()

    while timeout > 0:
        reduce = get_offset(minimum, maximum)
        timeout -= reduce

        keyboard.press(Key.space)
        keyboard.release(Key.space)

        # keyboard.press(Key.backspace)
        # keyboard.release(Key.backspace)
        # reduce -= 1
        # time.sleep(1)

        # Left time
        h = timeout // 3600
        timeout -= h * 3600
        m = timeout // 60
        s = timeout % 60

        info(f'\r   - {reduce} sec')
        echo(f'{h:02}:{m:02}:{s:02}')

        time.sleep(reduce)

    nl(2)
    success('DONE')


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        nl(1)
        echo('Shutting down...', bold=True, color='white')
        nl(1)

