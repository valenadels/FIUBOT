import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from aiohttp import request

#vinculo el botardo con esta app
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='+', intents=intents) #con + invoco al botardo
   
@bot.command(name='aiuda')
async def help(ctx):
    response = 'Binvenido/a! Este es un bot de autogestión FIUBA. Puedo hacer estas cosas:'+'\n-descargar el pdf de materias aprobadas del siu: +siuuu'+'\n-abrir tu campus: +campus'+'\n-mostrarte tu fiuba map: +fiubamap'
    await ctx.send(response)
    
@bot.command(name='siuuu')
async def siu_guarani(ctx):
    embed = discord.Embed()
    url_materias = "https://guaraniautogestion.fi.uba.ar/g3w/historia_academica/exportar_pdf/?checks=PromocionA,ExamenA,EquivalenciaA,AprobResA,&modo=materia&param_modo="
   
    embed.description = "Descargá tu pdf de materias aprobadas: [materias fiuba]("+url_materias+")."
    await ctx.send(embed=embed)


        
bot.run(TOKEN)
    