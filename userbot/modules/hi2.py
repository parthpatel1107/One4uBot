''' Whatever Plugin by Noobs of Telegram i.e. @TeleBotComms
    custom cmd: .hi2
'''

from telethon import events
import asyncio
import os
import sys
from userbot.events import register

@register(outgoing=True, pattern=r"^.hi2(?: |$)(.*)")
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("🌺✨✨🌺✨🌺🌺🌺\n🌺✨✨🌺✨✨🌺✨\n🌺🌺🌺🌺✨✨🌺✨\n🌺✨✨🌺✨✨🌺✨\n🌺✨✨🌺✨🌺🌺🌺\n☁☁☁☁☁☁☁☁")



