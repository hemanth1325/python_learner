import threading
import time

def race(durations):
    """
    Start one thread per duration. Each thread sleeps for its duration
    then records its index. Return the list of indices in finish order.
    """
    results = []
    threads = []

    def worker(index, duration):
        time.sleep(duration)
        results.append(index)

    for i, d in enumerate(durations):
        t = threading.Thread(target=worker, args=(i, d))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    return results

if __name__ == "__main__":
    # Type your input separated by spaces, for example: 2 0.5 1
    durations = [float(x) for x in input().split()]
    print(race(durations))
