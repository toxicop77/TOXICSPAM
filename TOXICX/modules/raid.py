import asyncio
import random
from telethon import events
from config import TX1, TX2, TX3, TX4, TX5 , TX6, TX7, TX8, TX9, TX10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from TOXICX.data import RAID, REPLYRAID, ALTRON, MRAID, SRAID, CRAID, ALTRON

que = {}


@TX1.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@TX2.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@TX3.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@TX4.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@TX5.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@TX6.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@TX7.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@TX8.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@TX9.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@TX10.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝗥𝗮𝗶𝗱\n  » {hl}raid <count> <Username of User>\n  » {hl}raid <count> <reply to a User>"
    if e.sender_id in SUDO_USERS:
        TXraid = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)

        if len(TXraid) == 2:
            message = str(TXraid[1])
            a = await e.client.get_entity(message)
            g = a.id
            if int(g) in TOXIC:
                await e.reply("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ TOXIC'ꜱ ᴏᴡɴᴇʀ", parse_mode=None, link_preview=None)
            elif int(g) in SUDO_USERS:
                await e.reply("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ", parse_mode=None, link_preview=None)
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(TXraid[0])
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in TOXIC:
                await e.reply("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ TOXIC'ꜱ ᴏᴡɴᴇʀ", parse_mode=None, link_preview=None)
            elif int(g) in SUDO_USERS:
                await e.reply("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ", parse_mode=None, link_preview=None)
            else:
                c = b.first_name
                counter = int(TXraid[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

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
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    await asyncio.sleep(0.3)
    await event.client.send_message(
        entity=event.chat_id,
        message="""{}""".format(random.choice(REPLYRAID)),
        reply_to=event.message.id,
    )


@TX1.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@TX2.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@TX3.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@TX4.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@TX5.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@TX6.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@TX7.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@TX8.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@TX9.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@TX10.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
async def _(e):
    global que
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » {hl}rraid <Username of User>\n  » {hl}rraid <reply to a User>"
    if e.sender_id in SUDO_USERS:
        TXrr = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 11:
            message = str(mkrr[0])
            a = await e.client.get_entity(message)
            user_id = int(a.id)
            if int(user_id) in TOXIC:
                await e.reply("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ TOXIC'ꜱ ᴏᴡɴᴇʀ", parse_mode=None, link_preview=None)
            elif int(user_id) == OWNER_ID:
                await e.reply("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ", parse_mode=None, link_preview=None)
            elif int(user_id) in SUDO_USERS:
                await e.reply("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ", parse_mode=None, link_preview=None)
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                await e.reply("» ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ !! ✅", parse_mode=None, link_preview=None)

                elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            user_id = int(b.id)
            if int(user_id) in TOXIC:
                await e.reply("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ TOXIC'ꜱ ᴏᴡɴᴇʀ", parse_mode=None, link_preview=None)
            elif int(user_id) == OWNER_ID:
                await e.reply("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ", parse_mode=None, link_preview=None)
            elif int(user_id) in SUDO_USERS:
                await e.reply("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ", parse_mode=None, link_preview=None)
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                await e.reply("» ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ !! ✅", parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@TX1.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@TX2.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@TX3.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@TX4.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@TX5.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@TX6.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@TX7.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@TX8.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@TX9.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@TX10.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
async def _(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐃𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » {hl}drraid <Username of User>\n  » {hl}drraid <reply to a User>"
    global que    
    if e.sender_id in SUDO_USERS:
        TOXX = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)

        if len(e.text) > 12:
            message = str(TOXX[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception:
                pass
            await e.reply("» ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ !! ✅", parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception:
                pass
            await e.reply("» ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ !! ✅", parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)

            @TX1.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@TX2.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@TX3.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@TX4.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@TX5.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@TX6.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@TX7.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@TX8.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@TX9.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@TX10.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝗠𝗥𝗮𝗶𝗱\n  » {hl}mraid <count> <Username of User>\n  » {hl}mraid <count> <reply to a User>"
    if e.sender_id in SUDO_USERS:
        TXmr = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(TXmr) == 2:
            message = str(TXmr[1])
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(TXmr[0])
            for _ in range(counter):
                reply = random.choice(MRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(TXmr[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(MRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@TX1.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@TX2.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@TX3.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@TX4.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@TX5.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@TX6.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@TX7.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@TX8.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@TX9.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@TX10.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝗦𝗥𝗮𝗶𝗱\n  » {hl}sraid <count> <Username of User>\n  » {hl}sraid <count> <reply to a User>"
    if e.sender_id in SUDO_USERS:
        TXsr = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(MKsr) == 2:
            message = str(TXsr[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(TXsr[0])
            for _ in range(counter):
                reply = random.choice(SRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(TXsr[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(SRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@TX1.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@TX2.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@TX3.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@TX4.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@TX5.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@TX6.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@TX7.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@TX8.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@TX9.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@TX10.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: C𝗥𝗮𝗶𝗱\n  » {hl}craid <count> <Username of User>\n  » {hl}craid <count> <reply to a User>"
    if e.sender_id in SUDO_USERS:
        TXsr = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(TXsr) == 2:
            message = str(TXsr[1])
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(TXsr[0])
            for _ in range(counter):
                reply = random.choice(CRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(TXsr[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(CRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
