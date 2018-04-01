import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import datetime

Client = discord.Client()
client = commands.Bot(command_prefix = "E", description="E is the prefix.")


@client.command(pass_context=True)
async def ping(ctx):
    await client.say("hello world")

client.run("Bot token")
