from pynput import mouse, keyboard
import time


def stop_event(*args, **kwargs):
    global user_confirmed
    user_confirmed = time.time()
    print(' ')
    print('Stop Mouse event !')
    print(user_confirmed)


user_confirmed = 0

if __name__ == '__main__':

    listener = mouse.Listener(on_move=stop_event, on_click=stop_event, on_scroll=stop_event)
    listener.daemon = True
    listener.start()

    try:
        # with listener:
        while True:
            if user_confirmed:
                if round(time.time() - user_confirmed) > 10:
                    user_confirmed = 0
                    continue

                print('Wait 10 seconds...')
                time.sleep(10)
            else:
                print('Loop every 5 seconds...')
                time.sleep(5)

    except KeyboardInterrupt:
        print('\nShutting Down...\n')

    finally:
        listener.stop()
