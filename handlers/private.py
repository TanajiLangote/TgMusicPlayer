from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2




START_TEXT = """
Hello {} I am an Telegram Groups Music Player, I let you play music in your group's voice chat.
"""

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel', url="https://t.me/TeleVcplayer")
        ]]
  
)

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
   
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTON,
        disable_web_page_preview=True,
        quote=True
    )

