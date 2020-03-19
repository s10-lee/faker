#
# Get PID
#   process = subprocess.run(['pgrep', 'firefox'], stdout=subprocess.PIPE)
#   process.stdout.decode()
#
# Open applications:
#   open index.js -a Visual\ Studio\ Code.app
#   open https://ya.ru -a Firefox
#
# Activate application
#   osascript -e 'tell application "PyCharm" to activate'
#
# List all gui application
#   osascript -e 'tell application "System Events" to get name of (processes where background only is false)'
#
#
#
#
# Subprocess examples
#   process = subprocess.Popen(['pgrep', 'firefox'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#   my_pid, err = process.communicate()
#   print(bytes(my_pid).decode())
#
# Examples 2
#   command = ['osascript', '-e',
#              'tell application "System Events" to get name of (processes where background only is false)']
#   process = subprocess.run(command, stdout=subprocess.PIPE)
#   print(process.stdout)
#
import subprocess
from pynput.keyboard import Key, Controller as cone
from pynput.mouse import Button, Controller as ctwo
from random import randint
# import sys
import time

# Init
keyboard = cone()
mouse = ctwo()


def terminal_command(*args):
    process = subprocess.run(args, stdout=subprocess.PIPE)
    return process.stdout.decode().strip()


def get_countdown(remain_time):
    countdown = ''
    h, m, s = 0, 0, 0
    rt = remain_time

    if rt > 3600:
        h = rt // 3600
        rt -= h * 3600

    if rt > 60:
        m = rt // 60
        rt -= m * 60

    if rt > 0:
        s = rt

        if s:
            countdown = f'{m:02}:{s:02}'
            if h:
                countdown = f'{h:02}:{countdown}'
    return countdown


def get_active_apps():
    command = ['osascript',
               '-e',
               'tell application "System Events" to get name of (processes where background only is false)']
    process = subprocess.run(command, stdout=subprocess.PIPE)
    result = [n.strip() for n in process.stdout.decode().split(',')]
    return result


def show_app(app_name):
    command = ['osascript',
               '-e',
               f'tell application "{app_name}" to activate']
    process = subprocess.run(command, stdout=subprocess.PIPE)
    result = [n.strip() for n in process.stdout.decode().split(',')]
    return result


def press_key(char):
    delay = randint(50, 500) / 1000

    if char == '\n':
        char = Key.enter

    keyboard.press(char)
    keyboard.release(char)
    time.sleep(delay)
    return delay


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
