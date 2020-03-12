from src.mixins import success, info, echo, ask, nl, h1, confirm
from src.utils import get_source, get_console_option, write_code, get_random, open_chrome
import time
import sys
import subprocess
from random import randint, randrange, choice
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as CTRL
mouse = Controller()
keyboard = CTRL()

def run():

    #
    #   TODO: Remove this crap !
    #
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

    #
    #   Source Code
    #
    source = get_source(get_console_option(['-p', '--path']))

    #
    #   Timeout
    #
    timeout = get_console_option(['-t', '--time', '--timeout'], int)
    if not timeout:
        timeout = ask('Timeout in minutes ?', default=10, greater=5)
        nl()
    echo(f'timeout {timeout} minutes', color='white')
    timeout *= 60
    nl(1)

    #
    #   Interval
    #
    minimum = get_console_option(['-i', '--int', '--interval'], int)
    if not minimum:
        minimum = ask('Interval in seconds', greater=5, default=12)
        nl()
    echo(f'interval {minimum} sec', color='white')
    nl(1)

    #
    #   Maximum Interval
    #
    m = 20
    if minimum > m:
        m = minimum
    maximum = ask('Maximum interval ', greater=minimum, default=m)
    if maximum:
        nl()
        echo(f'max interval {maximum} sec', color='white')
    nl(2)

    #
    #   URL
    #
    url = get_console_option(['--url', '-u'])

    # sys.exit(1)

    #
    #   CountDown if source exists and confirmed
    #
    if source:
        check = confirm('Start dictating code from a source ? (yes/no)', default=False)
        echo('Yes' if check else 'No')

        if not check:
            source = False
    nl()

    if source:
        time.sleep(1)
        for i in range(3):
            echo(3 - i, bold=True, color='cyan')
            time.sleep(1)

    echo('START', bold=True, color='cyan')
    nl()

    start = 0
    x, y = 100, 100
    ut = 100
    url_timeout = 0
    while timeout > 0:

        reduce = get_random(minimum, maximum)
        timeout -= reduce
        length = reduce * 2
        sleep = reduce

        # RUN BROWSER
        if url and url_timeout <= 0:
            ut += reduce

        # Swap activity
        if ut > 60 * 2:
            ut = 0
            url_timeout = 60

            # CMD + TAB
            with keyboard.pressed(Key.cmd_l):
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)

            # Set Mouse
            mouse.position = (x, y)

        if url_timeout <= 0:
            with keyboard.pressed(Key.cmd_l):
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)

        if url_timeout > 0:
            url_timeout -= reduce

            # Move mouse
            x = randint(5, 0)
            mouse.move(x, y)

            if x >= 1000:
                x, y = 100, 100
                mouse.position = (x, y)

        elif source:
            code = source[start:start + length]
            spent = write_code(code)
            sleep = round(reduce - spent, 2)
            start += length

        h = timeout // 3600
        time_left = timeout - h * 3600
        m = time_left // 60
        s = time_left % 60

        countdown = f'{m:02}:{s:02}'
        if h:
            countdown = f'{h:02}:{countdown}'

        info(f'\r   - {reduce} sec', bold=True)
        echo(countdown, bold=True)
        nl()
        time.sleep(sleep)

    nl(2)
    success('DONE')


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        nl(1)
        echo('Shutting down...', bold=True, color='white')
        nl(1)

