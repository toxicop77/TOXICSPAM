from config import TX1, TX2, TX3, TX4, TX5, TX6, TX7, TX8, TX9, TX10, SUDO_USERS, CMD_HNDLR as hl
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon import events

@TX1.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@TX2.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@TX3.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@TX4.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@TX5.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@TX6.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@TX7.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@TX8.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@TX9.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@TX10.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
async def leave(e):
    if e.sender_id in SUDO_USERS:
        TXl = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)

        if len(e.text) > 7:
            event = await e.reply("» ʟᴇᴀᴠɪɴɢ...")
            try:
                await event.client(LeaveChannelRequest(int(TXl[0])))
            except Exception as e:
                await event.edit(str(e))
        else:
             if e.is_private:
                  alt = f"» ʏᴏᴜ ᴄᴀɴ'ᴛ ᴅᴏ ᴛʜɪꜱ ʜᴇʀᴇ !!\n\n» {hl}leave <ᴄʜᴀɴɴᴇʟ/ᴄʜᴀᴛ ɪᴅ> \n» {hl}leave : ᴛʏᴘᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ, ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ɢʀᴏᴜᴘ."
                  await e.reply(alt)
             else:
                  event = await e.reply("» ʟᴇᴀᴠɪɴɢ...")
                  try:
                      await event.client(LeaveChannelRequest(int(e.chat_id)))
                  except Exception as e:
                      await event.edit(str(e))
