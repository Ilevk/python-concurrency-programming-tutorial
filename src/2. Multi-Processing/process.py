import multiprocessing

def compute_bound(n):
   print(f"Worker process id for {n}: {multiprocessing.current_process().pid}")
   result = 1
   for i in range(2**18):
       result *= n
   return result

if __name__ == "__main__":
   process = multiprocessing.Process(target=compute_bound, args=(5,))
   process.start()
   print("Main process id: ", multiprocessing.current_process().pid)
   process.join()
