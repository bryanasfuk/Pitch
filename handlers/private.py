from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Aloo, Aku {bn} 🎵

Music Bot Group [Syntyche](t.me/syntychegroup) & [FvckgPrtnr](t.me/grupasikkchekk) . Manage by [♏ol](https://t.me/betterthaanhecan).

Add meGausa dipake Bot Jelek:p!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://github.com/ImJanindu/GroupMusicBot")
                  ],[
                    InlineKeyboardButton(
                        "Find On Group", url="https://t.me/syntychegroup"
                    ),
                    InlineKeyboardButton(
                        "Join Channel", url="https://t.me/ruangpublikk"
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
                        "Official Group", url="https://t.me/syntychegroup")
                ]
            ]
        )
   )


