#!/usr/bin/env python3
import os
import asyncio
import aiohttp

async def download_file(session, i):
    filename = f"sn-{i:03d}.txt"
    url = f"https://www.grc.com/sn/{filename}"
    dest = os.path.join('transcripts', filename)
    async with session.get(url) as resp:
        if resp.status == 200:
            content = await resp.read()
            with open(dest, 'wb') as f:
                f.write(content)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed: {filename}")

async def async_main():
    os.makedirs('transcripts', exist_ok=True)
    indices = range(1, 1200)
    async with aiohttp.ClientSession() as session:
        tasks = [download_file(session, i) for i in indices]
        await asyncio.gather(*tasks)

def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()
