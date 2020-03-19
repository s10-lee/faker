from src.utils import get_countdown, show_app
from src.terminal import Terminal
from src.apps import VSCode, Firefox, Safari, Faker, Skype, Telegram
import time
import sys
from random import randint


# Terminal
terminal = Terminal(timeout=('t', 'time', 'timeout'), path=('p', 'path'))

# Faker
faker = Faker(terminal)

vscode = VSCode(terminal.get_arg('path'))
vscode.open('./_source/index.js')

firefox = Firefox()
telegram = Telegram()


# class Schedule:
#     def __init__(self, t, a):
#         self.timeout = t
#         self.main = a
#         self.timeline = {t: a}
#
#     def planning(self, app, t, offset=120):
#         self.timeout -= t * 60
#         if self.timeout > 0:
#             self.timeline[self.timeout] = app
#
#         if self.timeout - offset > 0:
#             self.timeout -= offset
#             self.timeline[self.timeout] = self.main


def run():

    timeout = int(terminal.get_arg('timeout', 60))
    terminal.write(f'Timeout {timeout} minutes', color='white')
    timeout *= 60

    for i in range(3):
        terminal.write(3 - i, bold=True, color='cyan')
        time.sleep(1)
    terminal.write('START', bold=True, color='cyan')

    while timeout > 0:

        reduce = randint(8, 14)
        if reduce > timeout:
            reduce = timeout
        timeout -= reduce
        sleep = reduce

        if vscode.code:
            spent = vscode.write(reduce * 2)
            sleep = round(reduce - spent)

        terminal.write(f'\n - {reduce:02} sec', color='cyan', bold=True)
        terminal.write(get_countdown(timeout), bold=True)

        time.sleep(sleep)

    terminal.write('\r\nDONE\r\n')


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        terminal.write('\r\nShutting down...\r\n', bold=True, color='white')

