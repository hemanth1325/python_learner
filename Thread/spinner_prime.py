import threading
import itertools
import sys
import time
import math


def is_prime(n: int) -> bool:
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
    return True


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


def supervisor(n):
    signal = Signal()

    spinner = threading.Thread(target=spin, args=("checking prime!", signal))
    spinner.start()

    result = is_prime(n)

    signal.go = False
    spinner.join()

    return result


def main():
    n = 5000111000222021
    result = supervisor(n)
    print(f"Is {n} prime? {result}")


if __name__ == "__main__":
    main()