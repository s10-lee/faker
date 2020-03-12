from pynput.keyboard import Key, Controller
import time
import sys

SCHEMA = {
    'red': '31',
    'green': '32',
    'yellow': '33',
    'blue': '34',
    'purple': '35',
    'cyan': '36',
    'gray': '37',
    'white': '38',
}


def color_text(text, color):
    return f"\033[1;{SCHEMA.get(color, '37')}m{text}\033[0m"


def run(total, interval):
    steps = total // interval + total % interval
    print('\r\n')
    print(color_text('START', 'green'))
    keyboard = Controller()
    while steps > 0:
        keyboard.press(Key.space)
        keyboard.release(Key.space)

        print('\r -', color_text(f'{steps * interval // 60}:{steps * interval % 60:02}', 'cyan'))

        # keyboard.press(Key.backspace)
        # keyboard.release(Key.backspace)
        time.sleep(interval)
        steps -= 1

    print('\r', color_text('DONE', 'green'), sep='')
    print('\r\n')


if __name__ == '__main__':

    # Total idle time to faking (in minutes)
    total_idle = 5

    # Trigger keyboard event every N seconds
    interval_in_seconds = 10

    if len(sys.argv) > 1:
        for index, argument in enumerate(sys.argv):
            if argument in ['--interval', '-i'] and len(sys.argv) > index + 1:
                interval_in_seconds = int(sys.argv[index + 1])

            if argument in ['--total', '-t'] and len(sys.argv) > index + 1:
                total_idle = int(sys.argv[index + 1])

    try:
        run(total_idle * 60, interval_in_seconds)
    except KeyboardInterrupt:
        print('\r\n')
        print(color_text('Shutting down...', 'green'))

