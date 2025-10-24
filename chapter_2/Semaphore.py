from code import do_something
import time
import threading

if __name__ == "__main__":
    size = 10000000
    counts = [5]

    print("\nSemaphore")
    for threads in counts:
        semaphore = threading.Semaphore(3) 
        jobs = []
        start_time = time.time()

        def safe_do_something(size, out_list):
            with semaphore:
                do_something(size, out_list)

        for i in range(threads):
            out_list = []
            thread = threading.Thread(target=safe_do_something, args=(size, out_list))
            jobs.append(thread)

        for t in jobs:
            t.start()
        for t in jobs:
            t.join()

        end_time = time.time()
        print(f"Threads (Semaphore): {threads}, Time taken = {end_time - start_time:.2f} seconds")

    print("\nAll processing complete.")
