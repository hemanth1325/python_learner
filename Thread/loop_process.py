import multiprocessing
import time

def run_loop(process_id):
    start_time = time.perf_counter()
    
    for i in range(10000):
        print(i)
    end_time = time.perf_counter()
    exec_time = end_time - start_time
    print(f"Process {process_id} execution time: {exec_time:.4f} seconds")

if __name__ == "__main__":
    processess=[]
    for p in range(3):
        process = multiprocessing.Process(target=run_loop, args=(p,))
        processess.append(process)

    overall_start_time = time.perf_counter()

    for process in processess:
        process.start()

    for process in processess:
        process.join()

    overall_end_time = time.perf_counter()
    overall_exec_time = overall_end_time - overall_start_time
    print(f"Overall execution time: {overall_exec_time:.4f} seconds")