import threading
import itertools
import sys
import time

class Signal:
    go = True

def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        time.sleep(0.1)
        if not signal.go:
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
    signal = Signal()

    spinner = threading.Thread(
        target=spin,
        args=('thinking!', signal)
    )

    spinner.start()

    result = run_loop(1)

    signal.go = False
    spinner.join()

    return result

def main():
    result = supervisor()
    print("Execution Time:", result)

if __name__ == '__main__':
    main()