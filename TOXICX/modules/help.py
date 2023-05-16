from config import TX1, TX2, TX3, TX4, TX5, TX6, TX7, TX8, TX9, TX10, SUDO_USERS, CMD_HNDLR as hl
from telethon import events, Button


PythonHelp = f"★ 𝙏𝙊𝙓𝙄𝘾 𝙓 𝙎𝙋𝘼𝙈 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪 ★\n\n» **ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ꜰᴏʀ ʜᴇʟᴘ**\n» **ᴅᴇᴠᴇʟᴏᴘᴇʀ: @MERA_JIJA_HAI_TU**"


@TX1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@TX2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@TX3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@TX4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@TX5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@TX6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@TX7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@TX8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@TX9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@TX10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  "https://graph.org/file/9ba2e1c637ca3d2809769.jpg",
                                  caption=PythonHelp,
                                  buttons=[
           [
            Button.inline("• ꜱᴘᴀᴍ •", data="spam"),
            Button.inline("• ʀᴀɪᴅ •", data="raid"),
           ],
           [
            Button.inline("• ᴇxᴛʀᴀ •", data="extra"),
           ],
           [    
            Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/KNOW_UR_JIJA"),
            Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/TOXIC_X_SUPPORT")
           ],
           ],
           )
