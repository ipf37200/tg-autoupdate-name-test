import time
import os
import sys
import logging
import asyncio
from time import strftime
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from emoji import emojize

number_emojis = {
    '0': emojize(":zero:", use_aliases=True),
    '1': emojize(":one:", use_aliases=True),
    '2': emojize(":two:", use_aliases=True),
    '3': emojize(":three:", use_aliases=True),
    '4': emojize(":four:", use_aliases=True),
    '5': emojize(":five:", use_aliases=True),
    '6': emojize(":six:", use_aliases=True),
    '7': emojize(":seven:", use_aliases=True),
    '8': emojize(":eight:", use_aliases=True),
    '9': emojize(":nine:", use_aliases=True),
}

api_auth_file = 'api_auth'
if not os.path.exists(api_auth_file + '.session'):
    api_id = input('api_id: ')
    api_hash = input('api_hash: ')
else:
    api_id = 
    api_hash = ''

client1 = TelegramClient(api_auth_file, api_id, api_hash)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def change_name_auto():
    print('will change name')

    while True:
        try:
            time_cur = strftime("%H:%M:%S:%p:%a", time.localtime())
            hour, minu, seco, p, abbwn = time_cur.split(':')
            if seco == '00' or seco == '30':
              
                hour_emoji = number_emojis[hour[0]] + number_emojis[hour[1]]  
                minute_emoji = number_emojis[minu[0]] + number_emojis[minu[1]] 
                last_name = f"{hour_emoji}:{minute_emoji}"  

                await client1(UpdateProfileRequest(last_name=last_name))
                logger.info('Updated -> %s' % last_name)

        except KeyboardInterrupt:
            print('\nwill reset last name\n')
            await client1(UpdateProfileRequest(last_name=''))
            sys.exit()

        except Exception as e:
            print('%s: %s' % (type(e), e))

        await asyncio.sleep(1)


# main function
async def main(loop):
    await client1.start()
    print('creating task')
    task = loop.create_task(change_name_auto())
    await task

    print('It works.')
    await client1.run_until_disconnected()
    task.cancel()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
