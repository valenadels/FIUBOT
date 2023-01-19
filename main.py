import os
from dotenv import load_dotenv
import json 
import urllib.request
import discord
from discord.ext import commands

#vinculo el botardo con esta app
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='+', intents=intents) #con esto invoco al botardo
   
@bot.command(name='ayudame_loco')
async def help(ctx):
    response = 'Binvenido/a! Este es un bot de autogestión FIUBA. Puedo hacer estas cosas:'+'\n-abrir tu siu: +siuuu'+'\n-abrir tu campus: +campus'+'\n-mostrarte tu fiuba map: +fiubamap'
    await ctx.send(response)
    
bot.run(TOKEN)
    