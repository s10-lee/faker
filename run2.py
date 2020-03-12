from src.mixins import success, info, echo, ask, nl, h1, echo_nl
from src.utils import get_source_from_files, get_source_files, get_console_option, write_code, get_random
import time

# SOURCE = get_source_from_files('adapters/http.js', 'adapters/xhr.js')
SOURCE = get_source_from_files('_source/axios.js')


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

    minutes = get_console_option(['-t', '--time', '--timeout'], int)
    if not minutes:
        minutes = ask('Total time in minutes ?', default=10, greater=5)
    echo(f'timeout {minutes} minutes')

    # Timeout to seconds
    timeout = minutes * 60

    path = get_console_option(['-p', '--path'])
    if path:
        get_source_files(path)

    minimum = get_console_option(['-i', '--int', '--interval'], int)
    if not minimum:
        minimum = ask('Minimum interval in seconds', greater=5, default=12)
    echo_nl(f'interval {minimum} sec')

    maximum = ask('Maximum interval, for random offset', greater=minimum + 1, default=20)
    if maximum:
        echo(f'max interval {maximum} sec')
        nl()
    nl(1)

    # CountDown
    time.sleep(1)
    for i in range(3):
        echo(3 - i, bold=True, color='cyan')
        time.sleep(1)
    echo('START', bold=True, color='cyan')
    nl()

    start = 0
    while timeout > 0:
        _before = time.perf_counter()

        reduce = get_random(minimum, maximum)
        timeout -= reduce
        length = reduce * 2

        code = SOURCE[start:start + length]
        spent = write_code(code)
        sleep = round(reduce - spent, 2)
        start += length

        h = timeout // 3600
        time_left = timeout - h * 3600
        m = time_left // 60
        s = time_left % 60

        echo(f'\r   - {reduce} sec, {length} chars, {spent} spent')
        echo(f'Left:  {h:02}:{m:02}:{s:02}')
        info(f'Sleep: {sleep} sec')

        time.sleep(sleep)
        echo(f'{round(time.perf_counter() - _before, 2)}', bold=True, color='yellow')

    nl(2)
    success('DONE')


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        nl(1)
        echo('Shutting down...', bold=True, color='white')
        nl(1)

