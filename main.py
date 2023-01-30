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
embed = discord.Embed(color=0x7C9FF7)

@bot.command(name='aiuda')
async def help(ctx):
    response = 'Binvenido/a! Este es un bot de autogestión FIUBA. Puedo hacer estas cosas:'+'\n- descargar el pdf de materias aprobadas del siu: +siuuu'+'\n- planner para organizar tu cursada: +planner'+'\n- fiuba map: +fiubamap'+'\n- materias electivas informática y sus créditos: +electivas'+'\n- calendario académico fiuba: +calendario'
    embed.description=response
    await ctx.send(embed=embed)
    
@bot.command(name='dolly')
async def opiniones(ctx):
    url_dolly = "https://dollyfiuba.com/resultados.html"
    embed.description = "Opiniones de cursos: [dolly fiuba]("+url_dolly+")."
    embed.set_thumbnail(url='https://dollyfiuba.com/img/DOLLY_LOGO.png')
    await ctx.send(embed=embed)
    
@bot.command(name='siuuu')
async def materias_aprobadas(ctx):
    url_materias = "https://guaraniautogestion.fi.uba.ar/g3w/historia_academica/exportar_pdf/?checks=PromocionA,ExamenA,EquivalenciaA,AprobResA,&modo=materia&param_modo="
    embed.description = "Descargá tu pdf de materias aprobadas: [materias fiuba]("+url_materias+")."
    await ctx.send(embed=embed)
    
@bot.command(name='planner')
async def planner(ctx):
    url_planner = "https://fede.dm/FIUBA-Plan/"
    embed.set_thumbnail(url="https://fede.dm/FIUBA-Plan/fplan.png")
    embed.description = "Este planner te va a ayudar a decidir qué materias cursar: [planner]("+url_planner+")."
    await ctx.send(embed=embed)

@bot.command(name='fiubamap')
async def map(ctx):
    url_map = "https://fede.dm/FIUBA-Map/"
    embed.description = "Abrí tu fiubamap: [fiubamap]("+url_map+")."
    embed.set_thumbnail(url="https://user-images.githubusercontent.com/37842382/111687719-5eb5fb80-8809-11eb-80f9-365c7bbc8811.png")
    await ctx.send(embed=embed)
    

@bot.command(name='calendario')
async def calendario_academico(ctx):
    await ctx.send(file=discord.File("recursos/Calendario_Academico_2023-2024.pdf"))
    
@bot.command(name='electivas')
async def electivas(ctx):
    await ctx.send(file=discord.File('recursos/electivas_informatica.pdf'))
    
 
@bot.event
async def on_member_join(member):
    await member.send('Hola! Bienvenido al servidor. Actualmente estas en el modo invitado. Por favor, ingresa tu padron para asi podes tener acceso completo.')
    
'''@bot.event
async def on_message(message):
    user_message = str(message.content)
    message_author = message.author

    if user_message == "107080":
      await  message_author.add_roles(atomic=True) 
'''
    


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Comando inválido. Si necesitas conocerlos tipeá: +aiuda")
        
bot.run(TOKEN)
    