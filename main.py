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
async def pokedex(ctx, theString : str):
    pokemon_name = pokes.get_pokemon_by_name(theString)
    for form in pokemon_name:
        embedPokedex = discord.Embed(title=form['name'] + " (" + form['number'] + ")", description="*The " + form['species'] + " Pokémon*", color=0x7289da)
        embedPokedex.add_field(name="Types:", value=", ".join(form['types']), inline=False)
        embedPokedex.add_field(name="Height:", value=form['height'], inline=False)
        embedPokedex.add_field(name="Weight:", value=form['weight'], inline=False)
        embedPokedex.add_field(name="Evolution Line:", value=" -> ".join(form['family']['evolutionLine']), inline=False)
        embedPokedex.add_field(name="Egg Groups:", value=", ".join(form['eggGroups']), inline=False)
        embedPokedex.set_thumbnail(url=form['sprite'])
        await client.say(embed=embedPokedex)
        
    

@client.command(pass_context=True)
async def pokedex2(ctx, theString : str):
    pokemon_name = pokes.get_pokemon_by_name(theString)
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


@client.command(pass_context=True)
async def pokedex3(ctx, theString : str):
    league = pokes.get_league(theString)
    embedPokedex = discord.Embed(title=league['name'], description="The " + league['region'] + " Region", color=0x7289da)
    embedPokedex.add_field(name="Badges:", value=", ".join(league['badges']), inline=False)
    embedPokedex.add_field(name="Badges Required:", value=league['badgesRequired'], inline=False)
    await client.say(embed=embedPokedex)

@client.command(pass_context=True)
async def pokedex4(ctx, theString : str):
    evostone = pokes.get_evolution_stone(theString)
    embedPokedex = discord.Embed(title=evostone['name'], description="aka " + evostone['aka'], color=0x7289da)
    embedPokedex.add_field(name="Effects:", value="\n".join(evostone['effects']), inline=False)
    embedPokedex.set_thumbnail(url=evostone['sprite'])
    await client.say(embed=embedPokedex)
    


        
        
    

    

    



        
        
    

    

    
client.run("The Token")
