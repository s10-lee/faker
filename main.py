from src.utils import get_countdown, press_key
from src.terminal import Terminal
from src.apps import VSCode, Firefox, Telegram
import time
import sys
from random import randint, choice


# Terminal
terminal = Terminal(timeout=('t', 'time', 'timeout'), path=('p', 'path'), interval=('i', 'interval'))

vscode = VSCode()
# terminal.get_arg('path')
# vscode.open('./_source/index.js')

firefox = Firefox()
telegram = Telegram()


def run():

    intervals = (
        (3, 5), (8, 10), (13, 15), (18, 20)
    )

    progress = 0
    interval_every = int(terminal.get_arg('interval', 10))
    interval_prev = 0
    interval = choice(intervals)
    terminal.write('******************')
    terminal.write(f'Interval {interval_every} min', color='white')
    terminal.write(f'Density {interval[0]} - {interval[1]} seconds', color='white')

    timeout = int(terminal.get_arg('timeout', 60))
    terminal.write(f'Timeout {timeout} min', color='white')
    timeout *= 60
    interval_every *= 60
    terminal.write('******************')

    for i in range(3):
        terminal.write(3 - i, bold=True, color='cyan')
        time.sleep(1)
    terminal.write('START', bold=True, color='cyan')

    while timeout > 0:

        reduce = randint(*interval)
        if reduce > timeout:
            reduce = timeout
        timeout -= reduce
        sleep = reduce

        if vscode.code:
            spent = vscode.write(reduce * 2)
            sleep = round(reduce - spent)
        else:
            press_key(' ')

        terminal.write(f'\n - {reduce:02} sec', color='cyan', bold=True)
        terminal.write(get_countdown(timeout), bold=True)

        progress += sleep

        if progress // interval_every > interval_prev:
            interval_prev = progress // interval_every
            interval = choice(tuple(filter(lambda x: x != interval, intervals)))
            terminal.write(f'Interval {interval}', color='white', bold=True)

        time.sleep(sleep)

    terminal.write('\r\nDONE\r\n')


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        terminal.write('\r\nShutting down...\r\n', bold=True, color='white')

