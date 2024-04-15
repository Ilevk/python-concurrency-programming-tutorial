import time
import requests

def io_bound(url):
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3",
        "https://jsonplaceholder.typicode.com/posts/4",
        "https://jsonplaceholder.typicode.com/posts/5"
    ]
    start = time.time()
    results = []
    for url in urls:
        results.append(io_bound(url))

    print(f"Time taken: {time.time() - start}, seconds")
