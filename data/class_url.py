import asyncio
import ast
import httpx



async def fetch(url, filename):
    """Simulate fetching a URL after 'delay' seconds."""
    r=httpx.get(url)
    text=r.text
    with open(f"data/{filename}.html", "w", ) as f:
        f.write(text)
        f.flush()
        
    return f"fetched: {url}"
    # TODO: return the string f"fetched: {url}"
    


async def _gather_all(url_delay_pairs):
    """Create and gather all fetch coroutines."""
    # TODO: build a list of fetch() coroutines from url_delay_pairs
    # TODO: return await asyncio.gather(*coroutines)
    coroutines = [fetch(url,delay) for url, delay in url_delay_pairs]
    return await asyncio.gather(*coroutines)


def fetch_all(url_delay_pairs):
    """Synchronous entry point. Runs the async event loop."""
    # TODO: use asyncio.run() to execute _gather_all
    # NOTE: Do NOT use asyncio.get_event_loop().run_until_complete() –
    #       asyncio.run() is the modern correct approach.
    return asyncio.run(_gather_all(url_delay_pairs))





if __name__ == "__main__":
    # pairs = ast.literal_eval(input())
    # print(fetch_all(pairs))

    
    pairs = [
        # ("https://www.example.com", 2),
        # ("https://www.python.org", 1),
        # ("https://www.asyncio.org", 3),
        ("https://www.mediadesign.de/de", )
    ]
    print(fetch_all(pairs))