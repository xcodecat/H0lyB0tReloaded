import lightbulb

moderation = lightbulb.Plugin("Moderation")

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(moderation)