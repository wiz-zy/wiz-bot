import requests
import datetime
import discord
import asyncio
import random
import logging
import random
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext.commands.cooldowns import BucketType
from asyncio import sleep
import json

now = datetime.datetime.now()
client = commands.Bot(command_prefix="-")
client.remove_command("help")


@client.event
async def on_ready():
    print(f"The time is {now.strftime('%B %d, %Y %H:%M:%S')}")
    print(f"Logged into {client.user}")
    activity = discord.Activity(
        name="coded by wizard#5236 /-/ Prefix: - ", type=discord.ActivityType.watching
    )
    await client.change_presence(activity=activity)


@commands.cooldown(1, 3, commands.BucketType.user)
@client.command()
async def bllist(ctx):
    with open("blacklist.json") as json_file:
        data = json.load(json_file)
        for id in data["users"]:
            if str(ctx.author.id) == str(id["id"]):
                await ctx.send("You're blacklisted from using commands!")
                return

        embed = discord.Embed(title=" ", color=0x659F67)
        embed.set_author(name=f"Wiz Bot's Blacklist", icon_url=ctx.author.avatar_url)
        embed.add_field(
            name="Blacklisted Users",
            value=f"""
```json\n
{json.dumps(data, indent=1)}
```
""",
            inline=True,
        )
        embed.set_footer(text="coded by wizard#5236")
        await ctx.send(embed=embed)


@commands.cooldown(1, 3, commands.BucketType.user)
@client.command()
async def blacklist(ctx, members: commands.Greedy[discord.Member], reason, time):
    if ctx.author.id == 325849904570302469:
        bldata = {}
        bldata["users"] = []
        embed = discord.Embed(title=" ", color=0xFF0000)
        embed.set_author(name="You've been blacklisted!")
        embed.add_field(name="Reason:", value=reason, inline=True)
        embed.add_field(name="Time:", value=time, inline=True)
        for member in members:
            bldata["users"].append({"user": str(member), "id": str(member.id)})
            await ctx.send(f"{member.mention} has been blacklisted!")
            await member.send(embed=embed)
        with open(
            "C:/Users/archmage/Documents/projection/blacklist.json", "w"
        ) as blacklist:
            json.dump(bldata, blacklist)
    else:
        await ctx.send(
            "You cannot blacklist users as you are not the owner of the bot!"
        )


@commands.cooldown(1, 3, commands.BucketType.user)
@client.command()
async def info(ctx, user: discord.Member):
    with open("blacklist.json") as json_file:
        data = json.load(json_file)
        for id in data["users"]:
            if str(ctx.author.id) == str(id["id"]):
                await ctx.send("You're blacklisted from using commands!")
                return

    embed = discord.Embed(title=" ", color=0x659F67)
    embed.set_author(name=f"Details of {user.name}", icon_url=user.avatar_url)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Highest Role", value=user.top_role, inline=True)
    embed.add_field(name="Join Date", value=user.joined_at, inline=True)
    embed.add_field(name="Created Account", value=user.created_at, inline=True)
    embed.set_footer(text="coded by wizard#5236")
    await ctx.send(embed=embed)


@commands.cooldown(1, 3, commands.BucketType.user)
@client.command()
async def ban(ctx, member: discord.Member, bantime, reason):
    with open("blacklist.json") as json_file:
        data = json.load(json_file)
        for id in data["users"]:
            if str(ctx.author.id) == str(id["id"]):
                await ctx.send("You're blacklisted from using commands!")
                return

        if member.bot == False or member == ctx.author or member == None:
            embed = discord.Embed(title=" ", color=0xFF0000)
            embed.set_author(name="Confirmation")
            embed.add_field(name="User:", value=f"<@{member.id}>", inline=True)
            embed.add_field(name="Time Banned for", value=bantime, inline=True)
            embed.add_field(name="Reason of ban", value=reason, inline=False)
            embed.set_footer(text=f"ID: {member.id}")
            message = await ctx.send(embed=embed)
            await message.add_reaction("✅")
            await message.add_reaction("🚫")

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in ["✅", "🚫"]

            try:
                reaction, user = await client.wait_for(
                    "reaction_add", timeout=60.0, check=check
                )
            except asyncio.TimeoutError:
                await member.send(
                    "asyncio.TimeoutError | You didn't react within 60 seconds. "
                )
                await message.delete()
            else:
                if reaction.emoji == "🚫":
                    await message.delete()
                    await message.clear_reactions()
                if reaction.emoji == "✅":
                    await ctx.guild.ban(member, reason=reason, delete_message_days=1)
                    await message.clear_reactions()
                    embed2 = discord.Embed(title=" ", color=0xFF0000)
                    embed2.set_author(name="User banned!")
                    embed2.add_field(name="User:", value=f"<@{member.id}>", inline=True)
                    embed2.add_field(name="Time Banned for", value=bantime, inline=True)
                    embed2.add_field(name="Reason of ban", value=reason, inline=False)
                    embed3 = discord.Embed(title=" ", color=0xFF0000)
                    embed3.set_author(name="You've gotten banned!")
                    embed3.add_field(name="User:", value=f"<@{member.id}>", inline=True)
                    embed3.add_field(name="Time Banned for", value=bantime, inline=True)
                    embed3.add_field(name="Reason of ban", value=reason, inline=False)
                    await message.edit(embed=embed2)
                    await member.send(embed=embed3)  # add server name later etc
        else:
            await ctx.send(
                "An error occured! Either the user was a bot or you tried to ban yourself, or you did not specify a member."
            )


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title="", color=0xA4CBFE)
        embed.set_author(name="Command Cooldown")
        embed.add_field(
            name="You can use this command in",
            value=f"{round(error.retry_after, 2)}s",
            inline=False,
        )
        embed.set_footer(text="coded by wizard#5236")
        await ctx.send(embed=embed)


client.run("ODE2MDg1NzM4MjU2MjAzNzk2.YD11Eg.ECfoqc_sgd3JPcMYQEmVK7BKGrk")
