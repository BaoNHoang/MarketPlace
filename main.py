import discord
from discord import commands

#test
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("The bot is active")

@client.command()
async def hello(ctx):
    await ctx.send("Hello I am ready to play")

client.run('MTI0MDMzNjg1ODI0NDcxNDY4Mg.GuUAld.rz-nKqDEkfIJde_vDVwmhTXnXKbxx6955lWwA0')