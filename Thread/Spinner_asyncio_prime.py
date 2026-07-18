import asyncio
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


async def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush

    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))

        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break

    write(' ' * len(status) + '\x08' * len(status))


async def supervisor(n):
    spinner = asyncio.create_task(spin("checking prime!"))

    result = await asyncio.to_thread(is_prime, n)

    spinner.cancel()

    return result


def main():
    n = 5000111000222021
    result = asyncio.run(supervisor(n))
    print(f"Is {n} prime? {result}")


if __name__ == "__main__":
    main()