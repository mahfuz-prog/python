import configparser
import time
from datetime import datetime
from winotify import Notification, audio
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.types import (
    PeerChannel
)

# Reading Configs
config = configparser.ConfigParser()
config.read("config-sample.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

#Notification
def notification(bid, stage):
    toast = Notification(app_id='my app', title=bid, msg=stage, duration='short')
    toast.set_audio(audio.LoopingAlarm, loop=True)
    return toast

#time formatting
def get_time(date_time):
    local_tz = datetime.now().astimezone().tzinfo
    local_time = date_time.astimezone(local_tz)
    new_date=local_time.strftime('%I:%M:%S %p')
    return new_date

#def 

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)

async def main(phone, notification, get_time):
    print("Client Created")
    # Ensure you're authorized
    if await client.is_user_authorized() == False:
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))
        
    me = await client.get_me()

    msg_input_channel = 163********
    msg_output_channel = 1854*********


    entity_input = PeerChannel(msg_input_channel)
    entity_output = PeerChannel(msg_output_channel)

    sender = await client.get_entity(entity_input)
    receiver = await client.get_entity(entity_output)
    
    while True:
        async for message in client.iter_messages (msg_input_channel, limit=1):
            res = [int(i) for i in message.text.split() if i.isdigit()]
            #print(res)
            for i in range(res.count(5)):
                res.remove(5)
            
            res = res[1:]
            res1 = res[-2:]
            
            print(get_time(message.date))
            print(res)
            #logic for notification and send message to channel
            if sum(res1) == 144:
                # await client.send_message(receiver, f'Stage 5, Suggested \
                # 	{int(sum(res1)/2)}, Time {get_time(message.date)}')
                notification(sum(res1)/2, 'stage 5').show()
                time.sleep(300)
            elif sum(res1) == 432:
                # await client.send_message(receiver, f'Stage 6, Suggested \
                # 	{int(sum(res1)/2)}, Time {get_time(message.date)}')
                notification(sum(res1)/2, 'stage 6').show()
                time.sleep(300)
            elif sum(res1) == 1296:
                # await client.send_message(receiver, f'Stage 7, Suggested \
                # 	{int(sum(res1)/2)}, Time {get_time(message.date)}')
                notification(sum(res1)/2, 'stage 7').show()
                time.sleep(300)
            elif sum(res1) == 3888:
                notification(sum(res1)/2, 'stage 8').show()
                time.sleep(300)
            else:
                print('Updating...')
                time.sleep(100)
            print('---------------------------------')

try:
    with client:
        client.loop.run_until_complete(main(phone, notification, get_time))
except:
    print('Error Occured')
