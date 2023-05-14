import glob
from pathlib import Path
from utils import load_plugins
import logging
import asyncio
from config import TX1, TX2, TX3, TX4, TX5, TX6, TX7, TX8, TX9, TX10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "TOXICX/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("\n𝙏𝙊𝙓𝙄𝘾 𝙓 𝙎𝙋𝘼𝙈 𝐒𝐩𝐚𝐦 𝐁𝐨𝐭𝐬 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 😎🤘🏻\nMy Master ---> @MERA_JIJA_HAI_TU")


async def main():
    await TX1.run_until_disconnected()
    await TX2.run_until_disconnected()
    await TX3.run_until_disconnected()
    await TX4.run_until_disconnected()
    await TX5.run_until_disconnected()
    await TX6.run_until_disconnected()
    await TX7.run_until_disconnected()
    await TX8.run_until_disconnected()
    await TX9.run_until_disconnected()
    await TX10.run_until_disconnected()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
