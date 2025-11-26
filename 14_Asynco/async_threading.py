
from concurrent.futures import ThreadPoolExecutor
import asyncio
import time

def check_stock(name):
    print(f"checking {name}....")
    time.sleep(3)
    return f"{name} has 30 stoks right now "

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock , "Masala chai")
        print(result)

asyncio.run(main())