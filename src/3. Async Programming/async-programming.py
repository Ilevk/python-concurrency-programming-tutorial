import asyncio
import aiohttp

async def io_bound(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = [
        'https://example.com/page1',
        'https://example.com/page2',
        'https://example.com/page3',
    ]

    tasks = [io_bound(url) for url in urls]
    results = await asyncio.gather(*tasks)

    for url, content in zip(urls, results):
        print(f"Content of {url}: {content[:100]}...")

if __name__ == "__main__":
    asyncio.run(main())
