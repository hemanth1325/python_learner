from multiprocessing import Process, Event
import sys
import itertools
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


def spin(msg, done: Event):
    write, flush = sys.stdout.write, sys.stdout.flush

    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))

        if done.wait(0.1):
            break

    write(' ' * len(status) + '\x08' * len(status))


def supervisor(n):
    done = Event()

    spinner = Process(target=spin, args=("checking prime!", done))
    spinner.start()

    result = is_prime(n)

    done.set()
    spinner.join()

    return result


def main():
    n = 5000111000222021
    result = supervisor(n)
    print(f"Is {n} prime? {result}")


if __name__ == "__main__":
    main()