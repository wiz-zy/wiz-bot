import requests
import datetime
import discord
import asyncio
import random
import logging
import os.path
import nekos
import hentai
from hentai import Hentai
import json
from hentai import Format
from urllib.parse import urlparse
from os.path import splitext
import random
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext.commands.cooldowns import BucketType
from asyncio import sleep
import json
import rule34
from dateutil.parser import parse

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


@client.group()
async def help(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(
            "NSFW: `-help nsfw` Administration: `-help admin` Commands: `-help commands`"
        )


@help.command()
async def nsfw(ctx):
    await ctx.send("test")


@help.command()
async def admin(ctx):
    await ctx.send("test")


@help.command()
async def command(ctx):
    await ctx.send("test")


@client.command()
async def keywords(ctx):
    possible = [
        "feet",
        "yuri",
        "trap",
        "futanari",
        "hololewd",
        "lewdkemo",
        "solog",
        "feetg",
        "cum",
        "erokemo",
        "les",
        "wallpaper",
        "lewdk",
        "ngif",
        "tickle",
        "lewd",
        "feed",
        "gecg",
        "eroyuri",
        "eron",
        "cum_jpg",
        "bj",
        "nsfw_neko_gif",
        "solo",
        "kemonomimi",
        "nsfw_avatar",
        "gasm",
        "poke",
        "anal",
        "slap",
        "hentai",
        "avatar",
        "erofeet",
        "holo",
        "keta",
        "blowjob",
        "pussy",
        "tits",
        "holoero",
        "lizard",
        "pussy_jpg",
        "pwankg",
        "classic",
        "kuni",
        "waifu",
        "pat",
        "8ball",
        "kiss",
        "femdom",
        "neko",
        "spank",
        "cuddle",
        "erok",
        "fox_girl",
        "boobs",
        "random_hentai_gif",
        "smallboobs",
        "hug",
        "ero",
        "smug",
        "goose",
        "baka",
        "woof",
    ]
    embed = discord.Embed(title=" ", color=0xFF0000)
    embed.set_author(name=" ")
    embed.add_field(name="Keywords", value=f"```{possible}```", inline=False)
    embed.set_footer(text="powered by nekos.life")
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    now = datetime.datetime.now()
    embed = discord.Embed(colour=discord.Colour.red())
    embed.set_author(name="Pong!")
    embed.set_footer(text=f"{round(client.latency * 1000)}ms")
    embed.timestamp = datetime.datetime.now()
    await ctx.send(embed=embed)


@client.command()
async def rantai(ctx):
    pictures = [
        "feet",
        "yuri",
        "trap",
        "futanari",
        "hololewd",
        "lewdkemo",
        "erokemo",
        "les",
        "lewdk",
        "lewd",
        "eroyuri",
        "eron",
        "cum_jpg",
        "bj",
        "solo",
        "kemonomimi",
        "nsfw_avatar",
        "erofeet",
        "holo",
        "keta",
        "blowjob",
        "tits",
        "holoero",
        "pussy_jpg",
        "kuni",
        "femdom",
        "neko",
        "erok",
        "boobs",
        "smallboobs",
        "ero",
    ]
    embed = discord.Embed(colour=discord.Colour.red())

    randomChoice = random.choice(pictures)
    embed.set_author(name=f'Sent an random NSFW picture with the tag "{randomChoice}"!')
    embed.set_image(url=nekos.img(randomChoice))
    embed.timestamp = datetime.datetime.now()
    embed.set_footer(text="Powered by nekos.life!")
    await ctx.send(embed=embed)


@client.command()
async def search(ctx, word):
    possible = [
        "feet",
        "yuri",
        "trap",
        "futanari",
        "hololewd",
        "lewdkemo",
        "solog",
        "feetg",
        "cum",
        "erokemo",
        "les",
        "wallpaper",
        "lewdk",
        "ngif",
        "tickle",
        "lewd",
        "feed",
        "gecg",
        "eroyuri",
        "eron",
        "cum_jpg",
        "bj",
        "nsfw_neko_gif",
        "solo",
        "kemonomimi",
        "nsfw_avatar",
        "gasm",
        "poke",
        "anal",
        "slap",
        "hentai",
        "avatar",
        "erofeet",
        "holo",
        "keta",
        "blowjob",
        "pussy",
        "tits",
        "holoero",
        "lizard",
        "pussy_jpg",
        "pwankg",
        "classic",
        "kuni",
        "waifu",
        "pat",
        "8ball",
        "kiss",
        "femdom",
        "neko",
        "spank",
        "cuddle",
        "erok",
        "fox_girl",
        "boobs",
        "random_hentai_gif",
        "smallboobs",
        "hug",
        "ero",
        "smug",
        "goose",
        "baka",
        "woof",
    ]

    if word in possible:
        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(name=f'Sent with the tag: "{word}"!')
        embed.set_image(url=nekos.img(word))
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text="Powered by nekos.life!")
        await ctx.send(embed=embed)
    else:
        await ctx.send("Invalid keyword.")


@client.command()
async def gentai(ctx):
    pictures = ["random_hentai_gif", "solog", "feetg", "cum", "pussy"]

    embed = discord.Embed(colour=discord.Colour.red())

    randomChoice = random.choice(pictures)
    embed.set_author(name=f'Sent with the tag: "{randomChoice}"!')
    embed.set_image(url=nekos.img(randomChoice))
    embed.timestamp = datetime.datetime.now()
    embed.set_footer(text="Powered by nekos.life!")
    await ctx.send(embed=embed)


@client.command()
async def dentai(ctx, number):
    cur_page = 1
    try:
        doujin = Hentai(number)
    except HTTPError:
        await ctx.send("You're stupid as fuck")
    pages = doujin.num_pages
    pages2 = doujin.num_pages - 1
    member = ctx.author
    embed = discord.Embed(colour=discord.Colour.red())
    embed2 = discord.Embed(colour=discord.Colour.red())
    embed.set_author(name="Would you like to read this Doujinshii?")
    embed.add_field(
        name=f"Doujin:", value=f"{doujin.title(Format.Pretty)}", inline=False
    )
    embed.add_field(name="Tags:", value=[tag.name for tag in doujin.tag], inline=False)
    embed.set_image(url=doujin.image_urls[0])
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
        await member.send("You didn't respond.")
        await message.delete()
    else:
        if reaction.emoji == "🚫":
            await ctx.send("Ok.")
            await message.delete()
            await message.clear_reactions()
        if reaction.emoji == "✅":
            await message.delete()
            embed2.set_author(
                name=f"Doujin: {doujin.title(Format.Pretty)} [Page: {cur_page}/{pages}]"
            )
            embed2.add_field(
                name="Tags:", value=[tag.name for tag in doujin.tag], inline=False
            )
            embed2.set_image(url=doujin.image_urls[0])
            embed2.timestamp = datetime.datetime.now()
            embed2.set_footer(text="Powered by NHentai")
            message = await ctx.send(embed=embed2)
            await message.add_reaction("◀")
            await message.add_reaction("▶")
            await message.add_reaction("✅")

            def check2(reaction, user):
                return user == ctx.author and str(reaction.emoji) in ["◀", "▶", "✅"]

            while True:
                try:
                    reaction, user = await client.wait_for(
                        "reaction_add", timeout=60.0, check=check2
                    )
                except asyncio.TimeoutError:
                    await member.send(
                        "You didn't read the next page of your doujinshii within 1 minute! Deleted your doujin."
                    )
                    await message.delete()
                    break
                else:
                    if reaction.emoji == "▶" and cur_page != pages:
                        cur_page += 1

                        embed3 = discord.Embed(colour=discord.Colour.red())

                        embed3.set_author(
                            name=f"Doujin: {doujin.title(Format.Pretty)} [Page: {cur_page}/{pages}]"
                        )
                        embed3.add_field(
                            name="Tags:",
                            value=[tag.name for tag in doujin.tag],
                            inline=False,
                        )
                        embed3.set_image(url=doujin.image_urls[cur_page - 1])
                        embed3.timestamp = datetime.datetime.now()
                        embed3.set_footer(text="Powered by NHentai!")
                        await message.edit(embed=embed3)
                        await message.remove_reaction(reaction, user)
                    if reaction.emoji == "✅":
                        embed5 = discord.Embed(colour=discord.Colour.red())

                        if cur_page != pages:
                            embed5.set_author(name=f"Doujin stopped at Page {cur_page}")
                            embed5.add_field(
                                name="Tags:",
                                value=[tag.name for tag in doujin.tag],
                                inline=False,
                            )
                            embed5.add_field(name=f"ID:", value=doujin.id, inline=False)
                            embed5.timestamp = datetime.datetime.now()
                            embed5.set_footer(text=f"{round(client.latency * 1000)}ms")
                            await message.edit(embed=embed5)
                            await message.clear_reactions()
                            break
                        else:
                            embed5.set_atuhor(name=f"Finished Doujin!")
                            embed5.add_field(
                                name="Tags:",
                                value=[tag.name for tag in doujin.tag],
                                inline=False,
                            )
                            embed5.add_field(name=f"ID:", value=doujin.id, inline=False)
                            embed5.timestamp = datetime.datetime.now()
                            embed5.set_footer(text=f"{round(client.latency * 1000)}ms")
                            await message.edit(embed=embed5)
                            await message.clear_reactions()
                            break
                    elif reaction.emoji == "◀" and cur_page != 0:
                        cur_page -= 1

                        embed4 = discord.Embed(colour=discord.Colour.red())

                        embed4.set_author(
                            name=f"Doujin: {doujin.title(Format.Pretty)} [Page: {cur_page}/{pages}]"
                        )
                        embed4.add_field(
                            name="Tags:",
                            value=[tag.name for tag in doujin.tag],
                            inline=False,
                        )
                        embed4.set_image(url=doujin.image_urls[cur_page - 1])
                        embed4.timestamp = datetime.datetime.now()
                        embed4.set_footer(text="Powered by NHentai!")
                        await message.edit(embed=embed4)
                        await message.remove_reaction(reaction, user)


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
async def r34(ctx, tag):
    r34 = rule34.Rule34(asyncio.get_running_loop())
    total_images = await r34.totalImages(tag)
    get_images = await r34.getImages(tags=tag, singlePage=True)
    image = get_images[int(1)]  # idfk man
    await ctx.send(
        f"""Total images: {total_images} 
        Tags: {image.tags} 
        Created at {image.created_at}"""
    )
    await ctx.send(image.file_url)


@commands.cooldown(1, 3, commands.BucketType.user)
@client.command()
async def ban(ctx, member: discord.Member, bantime, reason):
    with open("blacklist.json") as json_file:
        data = json.load(json_file)
        for id in data["users"]:
            if str(ctx.author.id) == str(id["id"]):
                await ctx.send("You're blacklisted from using commands!")
                return


        if (
            member.bot == False
            or member == ctx.author
            or member == None
        ):
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
            await ctx.send("An error occured while trying to ban this user.")


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


client.run("")
