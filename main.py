import hikari
import lightbulb

import os
import random
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import dotenv

dotenv.load_dotenv()

holy = lightbulb.BotApp(
    os.environ["BOT_TOKEN"],
    prefix="h!",
    banner=None,
    intents=hikari.Intents.ALL,
    default_enabled_guilds=(845711749944705035)
    )

if __name__ == "__main__":
    if os.name != "nt":
        import uvloop
        uvloop.install()

async def change_presence():
    number = random.choice([1, 2, 3])
    if number == 1:
        await holy.update_presence(status=hikari.Status.ONLINE, activity=hikari.Activity(name="Cheetah#7653", type=hikari.ActivityType.LISTENING))
    if number == 2:
        await holy.update_presence(status=hikari.Status.ONLINE, activity=hikari.Activity(name="Cheetah's Cat#4171 beim Programmieren zu", type=hikari.ActivityType.WATCHING))

if __name__ == "__main__":
  scheduler = AsyncIOScheduler()
  scheduler.add_job(change_presence, "interval", seconds=30)
  scheduler.start()


holy.load_extensions_from("./extensions/", must_exist=True)
holy.run()
