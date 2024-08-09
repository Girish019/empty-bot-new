
# from pyrogram import filters, Client
# from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
# from plugins.cbb import DATEDAY
# from bot import Bot
# from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON
# from helper_func import encode
# import re

from pyrogram import filters, Client, enums
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid, UsernameInvalid, UsernameNotModified
from config import ADMINS, LOG_CHANNEL, PUBLIC_FILE_STORE, WEBSITE_URL, WEBSITE_URL_MODE
from plugins.data import DATAODD, DATAEVEN ,BOTEFITMSG, FOMET
from plugins.users_api import get_user, get_short_link
from plugins.database import unpack_new_file_id
from datetime import datetime
from plugins.commands import DATEDAY
import re
import os
import json
import aiohttp
import asyncio
import requests
import string
import random
import base64
import logging


@Client.on_message(filters.private & filters.user(ADMINS) & filters.command(["date"]))
async def date(bot, message):
    dat = await message.reply_text("Select your Date.........",quote=True,
            reply_markup=InlineKeyboardMarkup(
                [[ 
                            InlineKeyboardButton("Yesterday",callback_data='ystdy'), 
                            InlineKeyboardButton("Today",callback_data = 'tdy'), 
                            InlineKeyboardButton("Tommorow",callback_data='tmr') 
                ]]
                                             ))
    

@Client.on_message(filters.private & filters.user(ADMINS) & ~filters.text)
async def channel_post(client: Client, message: Message):
    current_time = datetime.now()
    media = message.video or message.document
    
    bot_msg = await message.reply_text("Please Wait...!", quote = True) #reply text please wait... to bot
    try:
        #janvary = current_time.strftime("%B")
        medias = media.file_name.replace(".","_")
        filname = re.split("S\d\d", medias)[0]#[1][2]etc
        Eno= re.findall("S\d+E\d+\d", medias)
        if len(DATEDAY)==0:
            await client.send_message(chat_id=message.chat.id, text="Error: invalid date please set /date")
            bot_msg.delete()
            return 
        else:                
            if int(DATEDAY[-1][0:2]) % 2 != 0:#chaeking for ODD by given date
                if filname in DATAODD.keys(): #matching name in dict key with arrival video file name
                    await asyncio.sleep(1)
                    # chtid=int(DATAODD[filname][3])#for particular channel id
                    pic=DATAODD[filname][0] #particuler images
                    SL_URL=DATAODD[filname][1] #for particuler domine name
                    SL_API=DATAODD[filname][2] #for particuler api 
                   chtid=message.chat.id # if you want pic+formet into bot pm     
        
            elif int(DATEDAY[-1][0:2]) % 2 == 0: #checking for EVEN
                if filname in DATAEVEN.keys():
                    await asyncio.sleep(1)
                    # chtid=int(DATAEVEN[filname][3])
                    pic=DATAEVEN[filname][0]
                    SL_URL=DATAEVEN[filname][1]
                    SL_API=DATAEVEN[filname][2]
                    chtid=message.chat.id # if you want pic+formet into bot pm
            Size = await get_size(media.file_size)
            await bot_msg.edit("Getting size....!")
            await asyncio.sleep(1)
            Tlink = await convert_link(client , message)
            await bot_msg.edit("Tlink generating....!")
            await asyncio.sleep(1)
            Slink = await get_short(SL_URL, SL_API, Tlink)
            await bot_msg.edit("Slink generating....!")
            await asyncio.sleep(1)
            await bot_msg.edit("Sending post......!")
            await asyncio.sleep(1)
            if Slink:
                await client.send_photo(chat_id=chtid, photo=pic, caption=FOMET.format(DATEDAY[-1], Eno[0], Size, Slink, Slink))
                await bot_msg.edit(BOTEFITMSG.format(filname, Tlink, Slink, Size, DATEDAY[-1])) # msg edit in forwarder channel = "pic without captions (see line 41)" ==> thats return to our given format and short link ,date are updated here
                return 
            else:
                Slink = "ERORR_ACCURED"
                await message.reply_photo(photo=pic, caption=FOMET.format(DATEDAY[-1], Eno[0], Size, Slink, Slink), quote = True)
                await bot_msg.edit(f"<b>Here is your link</b>\n\n<code>{Tlink}</code>\n\n<b>Filename :</b> {medias}")
                return 
    except Exception as e:
        link = await conv_link(client , message)
        await bot_msg.edit(f"<b>Here is your link</b>\n\n{link}\n\n<code>{link}</code>\n\n<b>Exception couse :</b> {e}\n\n<b>Filename :</b> {medias}")
        Slink = "ERORR_ACCURED"
        await message.reply_photo(photo=pic, caption=FOMET.format(DATEDAY[-1], Eno[0], Size, Slink, Slink), quote = True)


async def convert_link(client, message):
    # username = (await bot.get_me()).username
    username = "PROFStrial_bot"
    file_type = message.media
    file_id, ref = unpack_new_file_id((getattr(message, file_type.value)).file_id)
    string = 'file_'
    string += file_id
    outstr = base64.urlsafe_b64encode(string.encode("ascii")).decode().strip("=")
    user_id = message.from_user.id
    share_link = f"https://t.me/{username}?start={outstr}"
    # await message.reply(f"<b>⭕ ʜᴇʀᴇ ɪs ʏᴏᴜʀ ʟɪɴᴋ:\n\n🔗 ᴏʀɪɢɪɴᴀʟ ʟɪɴᴋ :- {share_link}</b>")
    return share_link

async def get_size(size):
    """Get size in readable format"""

    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.1f %s" % (size, units[i])

async def get_short(SL_URL, SL_API, Tlink): #generating short link with particular domine and api
    try:
       api_url = f"https://{SL_URL}/api"
       params = {'api': SL_API, 'url': Tlink}
       async with aiohttp.ClientSession() as session:
           async with session.get(api_url, params=params) as resp:
               data = await resp.json()
               url = data["shortenedUrl"]
       return url
    except:
        resp = requests.get(f"https://{SL_URL}/api?api={SL_API}&url={Tlink}&alias={CustomAlias()}")
        data = resp.json()
        url = data["shortenedUrl"]  
        return url

def CustomAlias():
    # Generate a random integer between 3 and 8 (inclusive)
    length = random.randint(3, 8)
    # Define the population of characters to choose from
    population = string.ascii_letters + string.digits
    # Generate a random string of the specified length
    random_string = ''.join(random.choice(population) for _ in range(length))
    return random_string
