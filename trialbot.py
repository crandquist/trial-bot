import os
import random
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def new(ctx, day, time):
    response = 'A new trial has been created for {} at {}.'.format(day, time)
    await ctx.send(response)

bot.run(TOKEN)