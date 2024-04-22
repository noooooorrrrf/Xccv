import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

#          
                
@app.on_message(
    command(["المبرمج","نور","مطور السورس","مبرمج السورس"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2fd19ebe4a0ae1006b767.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[𓏺 ʏᴇѕ ɪ'ᴍ noor ˼](https://t.me/O_F_4)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @O_F_4 ❫
◉ 𝙸𝙳      : ❪ 5113311762 ❫
◉ 𝙱𝙸𝙾    : ❪ صلي علي الحبيب محمد ✨♥ ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᴅᴇᴠ noor", url=f"https://t.me/O_F_4"), 
                 ],[
                   InlineKeyboardButton(
                        "⌞ noor ⌝", url=f"https://t.me/NO_VP8"),
                ],

            ]

        ),

    )
