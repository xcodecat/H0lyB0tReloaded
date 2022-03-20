import lightbulb
import hikari

moderation = lightbulb.Plugin("Moderation")

@moderation.command
@lightbulb.option("target", "target to kick", hikari.User)
@lightbulb.command("kick", "Kicks a user")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def kick(ctx: lightbulb.Context) -> None:
    target = ctx.get_guild().get_member(ctx.options.target or ctx.user)
    if not target:
        await ctx.respond("That user is not in the server.")
        return
    await target.kick()
    await ctx.respond("Kicked!")

@moderation.command
@lightbulb.option("reason", "the reason for banning the member", str, required=False, modifier = lightbulb.commands.OptionModifier.CONSUME_REST)
@lightbulb.option("delete_message", "Delete the messages after the ban? (up to 7 days, leave empty or set to 0 to not delete)", int, min_value = 0, max_value = 7, default = 0 ,required=False)
@lightbulb.option("user", "the user you want to ban", hikari.User , required=True)
@lightbulb.command("ban", "ban a member")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def ban(ctx: lightbulb.Context, user, delete_message, reason):
    res = reason or f"'No Reason Provided.' By {ctx.author.username}"
    delete = delete_message or 0
    await ctx.respond(f"Banning **{user.username}**")
    await ctx.bot.rest.ban_member(user = user, guild = ctx.get_guild(), reason = res, delete_message_days=delete)
    await ctx.edit_last_response(f"Succesfully banned `{user}` for `{res}`!")
   

@moderation.command
@lightbulb.option("reason", "the reason for unbanning the member", str, required=False)
@lightbulb.option("user", "the user you want to unban (Please use their user ID)", hikari.Snowflake, required=True)
@lightbulb.command("unban", "unban a member")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def unban(ctx: lightbulb.Context,):
    ctx.options.reason or f"'No Reason Provided.' By {ctx.author.username}#{ctx.author.discriminator}"
    await ctx.respond(f"Unbanning the user ID of **{ctx.options.user}**")
    await ctx.bot.rest.unban_member(user = ctx.options.user, guild = ctx.get_guild(), reason = ctx.options.reason)
    await ctx.edit_last_response(f"Succesfully unbanned the ID of `{ctx.options.user}` for `{ctx.options.reason}`!")

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(moderation)