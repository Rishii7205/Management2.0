import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from MukeshRobot import SUPPORT_CHAT, pbot,BOT_USERNAME

PHOTO = [
    "https://te.legra.ph/file/634d6bb1e6b584d0140d2.jpg",
    "https://te.legra.ph/file/634d6bb1e6b584d0140d2.jpg",
    "https://te.legra.ph/file/634d6bb1e6b584d0140d2.jpg",
    "https://te.legra.ph/file/634d6bb1e6b584d0140d2.jpg",
    "https://te.legra.ph/file/634d6bb1e6b584d0140d2.jpg",
]

Mukesh = [
    [
        InlineKeyboardButton(text="📍𝐎𝐰𝐧𝐞𝐫📍", url=f"https://t.me/FUCK_THAT_AND_FUCK_YOU"),
        InlineKeyboardButton(text="🍒𝐆𝐫𝐨𝐮𝐩🍒", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="☆ 𝐀𝐝𝐝 𝐌𝐞 𝐌𝐨𝐢 𝐋𝐮𝐯 ☆",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

lol = "https://te.legra.ph/file/634d6bb1e6b584d0140d2.jpg"


@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("🖤")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await accha.delete()
    await asyncio.sleep(0.5)
    umm = await m.reply_sticker(
        "CAACAgUAAx0CYzn1-QACBNJkokXwQe20W4bcfiEZRNzwDcDtWgACcgoAAn392VT5P4ze45pHlR4E"
    )
    await umm.delete()
    await asyncio.sleep(0.8)
    await m.reply_photo(
        lol,
        caption=f"""**🌷ʜᴇʏ, ɪ ᴀᴍ 『[⏤‌•𝐓𝐆 ꭙ 𝐑𝐎𝐁𝐎𝐓](f"t.me/{BOT_USERNAME}")』🎄**
   ╔═════ஜ۩۞۩ஜ════╗

   ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 [𝐑𝐎𝐏𝐑𝐈𝐒𝐇](https://t.me/ABOUT_RISHU)♨️

   ╚═════ஜ۩۞۩ஜ════╝""",
        reply_markup=InlineKeyboardMarkup(Mukesh),
    )
__mod_name__ = "♨️ᴀʟɪᴠᴇ♨️"
__help__ = """

*ᴜsᴇʀ ᴄᴏᴍᴍᴀɴᴅs*:
» /alive*:* ᴛᴏ ᴄʜᴇᴀᴋ ❓  ɪ ᴀᴍ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ?

☆............𝙱𝚈 » [ㅤ𝄟͢🦋⃟≛⃝ 𝐌𝐑 𝄟⃝🖤🇬𝗛𝗢𝗦𝗧࿇ ](https://t.me/got_my_own_version)............☆"""
