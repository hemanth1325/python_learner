from multiprocessing import Process, Event
from multiprocessing import synchronize
import sys
import itertools
import time


def spin(msg, done: synchronize.Event):
    write, flush = sys.stdout.write, sys.stdout.flush

    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))

        if done.wait(0.1):
            break

    write(' ' * len(status) + '\x08' * len(status))


def run_loop(thread_id):
    start_time = time.perf_counter()

    for i in range(10000):
        print(i)

    end_time = time.perf_counter()
    exec_time = end_time - start_time

    print(f"\nThread {thread_id} execution time: {exec_time:.4f} seconds")

    return exec_time


def supervisor():
    done = Event()

    spinner = Process(target=spin, args=("thinking!", done))
    spinner.start()

    result = run_loop(1)   # Replaces slow_function()

    done.set()
    spinner.join()

    return result


def main():
    result = supervisor()
    print(f"Execution Time: {result:.4f} seconds")


if __name__ == '__main__':
    main()