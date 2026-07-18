import asyncio
import sys
import itertools
import time


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


async def run_loop(thread_id):
    start_time = time.perf_counter()

    for i in range(10000):
        print(i)

    end_time = time.perf_counter()
    exec_time = end_time - start_time

    print(f"\nThread {thread_id} execution time: {exec_time:.4f} seconds")

    return exec_time


async def supervisor():
    spinner = asyncio.create_task(spin("thinking!"))

    result = await run_loop(1)

    spinner.cancel()

    return result


def main():
    result = asyncio.run(supervisor())
    print(f"Execution Time: {result:.4f} seconds")


if __name__ == '__main__':
    main()