import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import datetime

Client = discord.Client()
client = commands.Bot(command_prefix = "E", description="E is the prefix.")

@client.event
async def on_command_error(ctx, error:discord.ext.commands.CommandError):
    errorid = False
    hasargs = False
    if isinstance(error,commands.MissingRequiredArgument):
        tprint("User did not provide enough arguments:")
        scui(ctx.guild,ctx.channel,ctx.author)
        errorid = True
        hasargs = True
        await client.ctx.send_message(ctx.message.channel, ":warning: **You haven't provided enough arguments!**.")



@client.command(pass_context=True)
async def ping(ctx):
    await client.say("{} Pong!".format(ctx.message.author.mention))

@client.command(pass_context=True)
async def kick(ctx, userName : discord.User):
    await client.kick(userName)
    await client.say("{} has been kicked. :white_check_mark:".format(userName))


@client.command(pass_context=True)
async def ban(ctx, userName : discord.User):
    await client.ban(userName)
    await client.say("{} has been banned. :white_check_mark:".format(userName))
        
        
    

    

    
client.run("Bot Token")
