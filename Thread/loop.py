import threading
import time

def run_loop(thred_id):
    start_time = time.perf_counter()
    
    for i in range(10000):
        print(i)
    end_time = time.perf_counter()
    exec_time = end_time - start_time
    print(f"Thread {thred_id} execution time: {exec_time:.4f} seconds")

threads=[]
for i in range(3):
    thread = threading.Thread(target=run_loop, args=(i,))
    threads.append(thread)

overall_start_time = time.perf_counter()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

overall_end_time = time.perf_counter()
overall_exec_time = overall_end_time - overall_start_time
print(f"Overall execution time: {overall_exec_time:.4f} seconds")