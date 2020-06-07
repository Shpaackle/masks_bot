import os
import random
from dotenv import load_dotenv

import discord
from discord.ext import commands
from dice_rolling import RollBuilder

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")
dice_roller = RollBuilder()
dice_roller.set_amount_of_dice(2)
dice_roller.set_number_of_sides(6)


@bot.event
async def on_ready():
    # guild = discord.utils.get(client.guilds, name=GUILD)
    # print(
    #    f"{client.user} is connected to the following guild:\n"
    #    f"{guild.name}(id: {guild.id})\n"
    # )
    print(f"{bot.user.name} has connected to Discord!")


@bot.command(name="roll", help="Rolls 2d6")
async def roll(ctx, sign: str = "+", bonus: int = 0):
    dice_roller.build()
    result = dice_roller.get_result()
    if sign == "-":
        bonus *= -1
    total = sum(result) + bonus
    response = f"{ctx.author.name} rolled a {total} ({result[0]} + {result[1]} + {bonus})"
    # print("rolling now")
    await ctx.send(response)


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Hi {member.name}, welcome to my Discord server!"
    )


bot.run(TOKEN)
