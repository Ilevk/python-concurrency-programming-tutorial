import threading
import requests

def io_bound(url):
   print("Thread is starting...")
   response = requests.get(url)
   print("Thread is ending...")

if __name__ == "__main__":
   url = "https://jsonplaceholder.typicode.com/posts/1"
   thread = threading.Thread(target=io_bound, args=(url,))
   thread.start()
   print("Main thread is waiting...")
   thread.join()

   print("Main thread is ending...")
