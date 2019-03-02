import asyncio
import os
import sys
import traceback

sys.path.append("..")  # Since examples are buried one level into source tree
from asyncpushbullet import AsyncPushbullet, InvalidKeyError, PushbulletError, LiveStreamListener

API_KEY = "o.3uyRuJaGGaD9AftYkIZZkbX1MreMMCeb"  # YOUR API KEY
PROXY = os.environ.get("https_proxy") or os.environ.get("http_proxy")
EXIT_INVALID_KEY = 1
EXIT_PUSHBULLET_ERROR = 2
EXIT_OTHER = 3


def main():
    async def _run():
        try:
            async with AsyncPushbullet(API_KEY, proxy=PROXY) as pb:

                # List devices
                devices = await pb.async_get_devices()
                print("Devices:")
                for dev in devices:
                    print("\t", dev)

                # Send a push
                push = await pb.async_push_note(title="Rasberry", body="System is online")
                print("Push sent:", push)

                # Ways to listen for pushes
                async with LiveStreamListener(pb) as lsl:
                    async for data in lsl:
                        if(data['source_device_iden:nickname']=="Xiaomi Mi A1" in data and data['body']=="leave" in data):
                            sys.exit(main())

        except InvalidKeyError as ke:
            print(ke, file=sys.stderr)
            return EXIT_INVALID_KEY

        except PushbulletError as pe:
            print(pe, file=sys.stderr)
            return EXIT_PUSHBULLET_ERROR

        except Exception as ex:
            print(ex, file=sys.stderr)
            traceback.print_tb(sys.exc_info()[2])
            return EXIT_OTHER

    loop = asyncio.get_event_loop()
    return loop.run_until_complete(_run())


if __name__ == "__main__":
    if API_KEY == "":
        with open("../api_key.txt") as f:
            API_KEY = f.read().strip()
    sys.exit(main())
