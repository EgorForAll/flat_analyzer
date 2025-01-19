import asyncio

async def parse_website(callee):
    return await asyncio.to_thread(callee)