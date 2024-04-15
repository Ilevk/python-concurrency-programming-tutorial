import concurrent.futures
import multiprocessing

def compute_bound(n):
    print(f"Worker process id for {n}: {multiprocessing.current_process().pid}")
    result = 1
    for i in range(2**18):
        result *= n
    return result

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(compute_bound, numbers))
    print("Main process id: ", multiprocessing.current_process().pid)
