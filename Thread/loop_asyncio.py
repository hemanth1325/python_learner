import asyncio
import time

async def run_loop(process_id):
    start_time = time.perf_counter()

    for i in range(10000):
        print(f"Task {process_id}: {i}")
        await asyncio.sleep(0)

    end_time = time.perf_counter()
    exec_time = end_time - start_time
    print(f"Task {process_id} execution time: {exec_time:.4f} seconds")


async def main():
    overall_start_time = time.perf_counter()

    await asyncio.gather(
        run_loop(0),
        run_loop(1),
        run_loop(2)
    )

    overall_end_time = time.perf_counter()
    print(f"Overall execution time: {overall_end_time - overall_start_time:.4f} seconds")


if __name__ == "__main__":
    asyncio.run(main())