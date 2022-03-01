import lightbulb

import random

fun = lightbulb.Plugin("Fun")

@fun.command()
@lightbulb.option("text", "Text to repeat")
@lightbulb.command("echo", "Repeats the user's input")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def echo(ctx: lightbulb.Context) -> None:
    await ctx.respond(ctx.options.text)

@fun.command()
@lightbulb.option("question", "Question to ask")
@lightbulb.command("8ball", "Answers a yes/no question")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def eightball(ctx: lightbulb.Context) -> None:
    await ctx.respond(random.choice(["Yes", "No", "Maybe", "I don't know"]))


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(fun)