import asyncio
import os
import sys
import traceback

sys.path.append("..")  # Since examples are buried one level into source tree
from asyncpushbullet import AsyncPushbullet, InvalidKeyError, PushbulletError, LiveStreamListener


async def _run():
    api_key = "o.3uyRuJaGGaD9AftYkIZZkbX1MreMMCeb"  # YOUR API KEY
    async with AsyncPushbullet(api_key) as pb:
        async with LiveStreamListener(pb) as pl:
            print("Awaiting pushes...")
            async for data in pl:
                print("Got a push:", data)

loop = asyncio.get_event_loop()
loop.run_until_complete(_run())
