import asyncio


async def add(n1, n2):
    print("sleeping for 2 sec before adding", n1, n2)
    await asyncio.sleep(2)
    return n1 + n2


# calling an async function using the await keyword

loop = asyncio.get_event_loop()
result = loop.run_until_complete(add(1,2))
print(result)
loop.close()