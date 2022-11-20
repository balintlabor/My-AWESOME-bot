import os

import discord
from discord.ext import commands


TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents, description="A simple Discord bot")


@bot.command(name="introduce", description="Introduces himself.")
async def foo(ctx, arg=""):
    res = arg if arg else "Hello, I am MY AWESOME BOT and I was created by Blint324 who is a great programmer and with the help of Geritwo and python i was created."
    await ctx.send(res)


@bot.command(name="meme", description="I watch to much SMG4...")
async def hello_user(ctx):
    await ctx.send(f"Niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiintendo memes...        I watch to much SMG4...")


@bot.command(name="server", description="Check server stats")
async def server_control(ctx, arg):
    pass

@bot.command(name="welcome", description="Welcomer.")
async def hello_user(ctx):
    await ctx.send(f"Hello {ctx.author}!")

@bot.command(name="botID", description="Sends botID.")
async def hello_user(ctx):
    await ctx.send(f"1043553836381503638")

@bot.command(name="fakeban", description="Fakebans a user.")
async def hello_user(ctx):
    await ctx.send(f"Sucessfully banned {ctx.author}. ")

@bot.command(name="commands", description="Sends all commands")
async def hello_user(ctx):
    await ctx.send(f"Try using ?fakeban to Fakeban somebody or ?botID to send the ID of this bot or ?welcome to welcome yourself becuse everybody knows discord users have no friends, or ?meme to send a classic or for another unfunny meme try using ?pog or ?urmom (I promise this is the last one)")

@bot.command(name="pog", description="Pog.")
async def hello_user(ctx):
    await ctx.send(f"Pog☠")

@bot.command(name="urmom", description="I promise this is the last unfunny joke.")
async def hello_user(ctx):
    await ctx.send(f"I think you forgot to put 's fat at the end.")

bot.run(TOKEN)
