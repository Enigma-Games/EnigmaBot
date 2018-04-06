import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from pokedex import pokedex

Client = discord.Client()
client = commands.Bot(command_prefix = "E", description="E is the prefix.")
pokes = pokedex.Pokedex(version="V1", user_agent="TheEBBGaming#4633 and Futuristick#7622")



@client.event
async def on_ready():
    print("ENIGMA'S AUTOMATION IS READY TO ROLL!")
    print("Pokedex.py loaded up.")
    
    



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
async def teams(ctx):
    em1 = discord.Embed(title="Team Valor, Team Mystic, or Team Instinct?", description="Do e<teamname> to assign a team role to yourself!", color=0x7146de)
    await client.say(embed=em1)
    
    

@client.command(pass_context=True)
async def instinct(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Team Instinct")
    await client.add_roles(user, role)
    await bot.say("Successfully added `Team Instinct` role to {}. :white_check_mark:".format(ctx.message.author.mention))


@client.command(pass_context=True)
async def mystic(ctx):
    user1 = ctx.message.author
    role1 = discord.utils.get(user.server.roles, name="Team Mystic")
    await client.add_roles(user1, role1)
    await bot.say("Successfully added `Team Mystic` role to {}. :white_check_mark:".format(ctx.message.author.mention))
    



@client.command(pass_context=True)
async def valor(ctx):
        user2 = ctx.message.author
        role2 = discord.utils.get(user.server.roles, name="Team Valor")
        await client.add_roles(user2, role2)
        await bot.say("Successfully added `Team Valor` role to {}. :white_check_mark:".format(ctx.message.author.mention))



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


@client.command(pass_context=True)
async def unban(ctx, userName : discord.User):
    await client.unban(userName)
    await client.say("{} has been unbanned. :white_check_mark:".format(userName))


@client.command(pass_context=True)
async def pokedex(ctx, theString: str):
    pokemon_name = pokes.get_pokemon_by_name(theString)
    await client.say(pokemon_name)

@client.command(pass_context=True)
async def pokedex2(ctx, theString : str):
    if theString == 'categories':
        categories = ["Starter","Legendary","Mythical","Ultra Beast","Mega"]
        await client.say(", ".join(categories))
    elif theString == 'egg-groups':
        egg_groups = ['Bug', 'Ditto', 'Dragon', 'Fairy', 'Field', 'Flying', 'Grass', 'Gender Unknown', 'Human-Like', 'Mineral', 'Monster', 'Amorphous', 'Undiscovered', 'Water 1', 'Water 2', 'Water 3']
        await client.say(", ".join(egg_groups))
    elif theString == 'evolution-stones':
        evolution_stones = pokes.get_evolution_stones()
        await client.say(", ".join(evolution_stones))
    elif theString == 'leagues':
        leagues = pokes.get_leagues()
        await client.say(", ".join(leagues))
        pokemon_name == pokes.get_pokemon_by_name(theSecondString)
        await bot.say(" ".join(pokemon_name))
    else:
        await client.say(":warning: Not found in Pokedex. Please note that all `pokedex` commands are case-sensitive. Do `Epokedex help` for more info.")
        
        
    

    

    



        
        
    

    

    
client.run("NDI5ODA5MjYzNTUzMDE5OTQ0.DaHCww.dmDuIr3MXON3t2ROEV79qt2xEzY")
