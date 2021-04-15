from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAADBQADnwEAAt7ZIVUGzRkM9dYMfQI")
    await message.reply_text(
        f"""**Eyo, Gua {bn} 🎵

Music Bot Group [LazyRich™](t.me/verylazyrich) & Manage by [bryan](https://t.me/deadasfck).

Kalo mau pake chat aja bryan!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://github.com/ImJanindu/GroupMusicBot")
                  ],[
                    InlineKeyboardButton(
                        "Find On Group", url="https://t.me/verylazyrich"
                    ),
                    InlineKeyboardButton(
                        "Join Channel", url="https://t.me/fckinganxiety"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/JEGroupMusicPlayerBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Official Group", url="https://t.me/verylazyrich")
                ]
            ]
        )
   )


