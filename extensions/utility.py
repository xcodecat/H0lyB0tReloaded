import hikari
import lightbulb

from datetime import datetime

utility = lightbulb.Plugin("Utility")

@utility.command
@lightbulb.option("target", "The member to get information about.", hikari.User, required=False)
@lightbulb.command("userinfo", "Get info on a server member.")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def userinfo(ctx: lightbulb.Context) -> None:
    target = ctx.get_guild().get_member(ctx.options.target or ctx.user)
    created_at = int(target.created_at.timestamp())
    joined_at = int(target.joined_at.timestamp())
    roles = (await target.fetch_roles())[1:]
    embed = (hikari.Embed(
            title=f"User Info - {target.display_name}",
            description=f"ID: `{target.id}`",
            colour=target.get_top_role().color if target.get_top_role() else 0xB33771,
            timestamp=datetime.now().astimezone(),)
        .set_footer(text=f"Requested by {ctx.member.display_name} • {ctx.author.id}", icon=ctx.member.avatar_url or ctx.member.default_avatar_url,)
        .set_thumbnail(target.avatar_url or target.default_avatar_url)
        .add_field("Bot?", str(target.is_bot), inline=True,)
        .add_field("Created account on", f"<t:{created_at}:d>\n(<t:{created_at}:R>)", inline=True,)
        .add_field("Joined server on", f"<t:{joined_at}:d>\n(<t:{joined_at}:R>)", inline=True,)
        .add_field("Roles", ", ".join(r.mention for r in roles) if roles else "Keine Rollen", inline=False,))
    await ctx.respond(embed)

@utility.command
@lightbulb.option("target", "Get the avatar of this user.", hikari.User, required=False)
@lightbulb.command("avatar", "Get the avatar of this user.")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def avatar(ctx: lightbulb.Context) -> None:
    target = ctx.get_guild().get_member(ctx.options.target or ctx.user)
    if not target:
        await ctx.respond("That user is not in the server.")
        return
    await ctx.respond(target.avatar_url or target.default_avatar_url)

@utility.command
@lightbulb.command("ping", description="The bot's ping")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"Pong! Latency: {utility.heartbeat_latency*1000:.2f}ms")

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(utility)