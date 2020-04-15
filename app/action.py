from pynput.mouse import Listener
import time
import sys
import multiprocessing as mp

status = False


def count():
    i = 0
    while True:
        i += 1
        time.sleep(1)
        print(f'{i} sec')


def watch(*args):
    global status
    if status:
        status = False
        print('mouse moved !')




listener = Listener(on_move=watch, on_click=watch, on_scroll=watch)
listener.start()
try:
    listener.wait()
    status = True
    i = 0
    while True:
        if not status:
            print('Wait 5 seconds')
            time.sleep(5)
            status = True

        i += 1
        time.sleep(1)
        print(f'{i} sec')


except KeyboardInterrupt:
    print('Exit...')

finally:
    listener.stop()
