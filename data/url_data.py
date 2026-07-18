import asyncio
import ast
import httpx
import os

async def fetch(url, delay):
    """Fetch URL and save content into data folder."""

    await asyncio.sleep(delay)

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    text = response.text

    # create folder if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # safe filename from URL
    filename = url.replace("https://", "").replace("http://", "")
    filename = filename.replace("/", "_")
    filepath = os.path.join("data", filename + ".html")

    # write file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

    return f"saved: {filepath}"


async def _gather_all(url_delay_pairs):
    coroutines = [fetch(url, delay) for url, delay in url_delay_pairs]
    return await asyncio.gather(*coroutines)


def fetch_all(url_delay_pairs):
    return asyncio.run(_gather_all(url_delay_pairs))


if __name__ == "__main__":
    # pairs = ast.literal_eval(input())

    pairs = [
        # ("https://www.example.com", 2),
        # ("https://www.python.org", 1),
        # ("https://www.asyncio.org", 3),
        ("https://www.mediadesign.de/de", 4),
    ]
    print(fetch_all(pairs))