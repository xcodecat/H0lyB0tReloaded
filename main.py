import os
import aiohttp

import dotenv
import hikari
import lightbulb

dotenv.load_dotenv()

bot = lightbulb.BotApp(
    os.environ["BOT_TOKEN"],
    prefix="h!",
    banner=None,
    intents=hikari.Intents.ALL,
    default_enabled_guilds=(845711749944705035))

@bot.command
@lightbulb.command("ping", description="The bot's ping")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"Pong! Latency: {bot.heartbeat_latency*1000:.2f}ms")

@bot.command()
@lightbulb.option("text", "Text to repeat")
@lightbulb.command("echo", "Repeats the user's input")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def echo(ctx: lightbulb.Context) -> None:
    await ctx.respond(ctx.options.text)

if __name__ == "__main__":
    if os.name != "nt":
        import uvloop
        uvloop.install()


    bot.load_extensions_from("./extensions/", must_exist=True)
    bot.run()
