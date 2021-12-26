#SDBOTs <https://t.me/SDBOTs_Inifinity>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SDSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SDSongBot import SDbot as app
from SDSongBot import LOGGER

pm_start_text = """
🤗Hey [{}](tg://user?id={}), I'm Song Downloader Bot🎵
Just send me the song name in this format.🤖 Don't only send the song name. It must in this below format👇
      eg:  ```/song Faded```
      eg:  ```/song Moonlight```
      
Developer: SanilaRanatunga✨️\n
Feedback : @sanilaassistant_bot
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    
                    InlineKeyboardButton(
                        text="Report Bugs😊", url="https://t.me/sanilaassistant_bot"
                    ),
                     InlineKeyboardButton(
                        text="Source Code🚥", url="https://github.com/sanila2007/Song-Download-Bot-"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("✅ MusicBot is online.")
idle()
