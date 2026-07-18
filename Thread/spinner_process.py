from multiprocessing import Process, Event
from multiprocessing import synchronize
import sys
import itertools
import time


def spin(msg, done: synchronize.Event):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + '' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        if done.wait(.1):
            break
    write(' '* len(status) + '\x08' * len(status))


def slow_function():
    time.sleep(3)
    return 110

def supervisor():
    done = Event()
    spinner = Process(target=spin, args=("thinking!", done))

    spinner.start()

    result = slow_function()

    done.set()
    spinner.join()

    return result

def main():
    result = supervisor()
    print(f"Answer: {result}")

if __name__ == '__main__':
    main()
