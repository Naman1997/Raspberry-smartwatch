import asyncio
import os
import sys
import traceback
import subprocess

sys.path.append("..")  # Since examples are buried one level into source tree
from asyncpushbullet import AsyncPushbullet, InvalidKeyError, PushbulletError, LiveStreamListener


async def _run():
    #MY API KEY
    api_key = "o.3uyRuJaGGaD9AftYkIZZkbX1MreMMCeb"
    async with AsyncPushbullet(api_key) as pb:
        async with LiveStreamListener(pb) as pl:
            print("Awaiting pushes...")
            push = await pb.async_push_note(title="Rasberry", body="System is online")
            print("Initialization response sent")
            async for data in pl:
                if('file_url' in data):
                    #For text to-do list feature in RPi
                    print('\n')
                    cmd = 'curl '+data['file_url']
                    name = data['file_name']
                    print("Filename = ",name)
                    os.system(cmd)
                    print('\n')
                elif('title' in data and data['title']=="Rasberry"):
                    #For response message by rasberry
                    pass
                elif('source_device_iden:nickname' in data and 'body' in data):
                    #For data sent via Pushbullet
                    if('title' in data and data['title']=="Rasberry"):
                        pass
                    else:
                        print('\n')
                        print(data['source_device_iden:nickname'])
                        print(data['body'])
                        push = await pb.async_push_note(title="Rasberry", body="Recieved")
                        print('\n')
                        if((data['body'])[0]=="$"):
                            print("Output:")
                            print('\n')
                            os.system((data['body'])[1:])
                            cmd=(data['body'])[1:].split()
                            push = await pb.async_push_note(title="Rasberry", body=subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0])
                        elif(data['body']=='exit'):
                            sys.exit()
                        print('\n')
                elif('push' in data and 'title' in data['push'] and 'body' in data['push']):
                    #For data sent via whatsapp
                    print('\n')
                    print(data['push']['title'])
                    print(data['push']['body'])
                    print('\n')
                else:
                    print("Got a push:", data)

loop = asyncio.get_event_loop()
loop.run_until_complete(_run())
