from telethon import events, Button
from config import TX1, TX2, TX3, TX4, TX5, TX6, TX7, TX8, TX9, TX10
from TOXICX.modules.help import *
import telethon

PythonButton = [
        [
        Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")
        ],
        [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/KNOW_UR_JIJA"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/TOXIC_X_SUPPORT")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/TOXICOP7755/TOXICSPAM")
        ]
        ]


@TX1.on(events.NewMessage(pattern="/start"))
@TX2.on(events.NewMessage(pattern="/start"))
@TX3.on(events.NewMessage(pattern="/start"))
@TX4.on(events.NewMessage(pattern="/start"))
@TX5.on(events.NewMessage(pattern="/start"))
@TX6.on(events.NewMessage(pattern="/start"))
@TX7.on(events.NewMessage(pattern="/start"))
@TX7.on(events.NewMessage(pattern="/start"))
@TX8.on(events.NewMessage(pattern="/start"))
@TX9.on(events.NewMessage(pattern="/start"))
@TX10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        TOXBot = await event.client.get_me()
        BotName = TOXBot.first_name
        BotId = TOXBot.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{BotName}](tg://user?id={BotId})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [TOXIC(PRIYANSHU)](https://t.me/MERA_JIJA_HAI_TU)**\n\n"
        TEXT += f"» **ʙᴏᴛ ꜱᴘᴀᴍ ᴠᴇʀsɪᴏɴ :** `M3.2`\n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{telethon.__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                event.chat_id,
                "https://graph.org/file/9ba2e1c637ca3d2809769.jpg",
                caption=TEXT, 
                buttons=PythonButton)
