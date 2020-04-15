from pynput.mouse import Listener
import time
import sys
import multiprocessing as mp


def count():
    i = 0
    while listener.running:
        i += 1
        time.sleep(1)
        print(f'{i} sec')


def watch(*args):
    print('Mouse moved !')
    return False


try:
    with Listener(on_move=watch, on_click=watch, on_scroll=watch) as listener:
        count()

except KeyboardInterrupt:
    print('Exit...')

