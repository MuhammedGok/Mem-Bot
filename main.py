
import discord
from discord.ext import commands
import os
import random
import requests

print(os.listdir('images'))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
@bot.command()
async def mem_mc(ctx):
    resimler_listesi = os.listdir("images")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'images/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def mem_gr(ctx):
    resimler_listesi2 = os.listdir("images2")
    rastgele_resim2 = random.choice(resimler_listesi2)
    with open(f'images2/{rastgele_resim2}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def mem_gow(ctx):
    resimler_listesi3 = os.listdir("images3")
    rastgele_resim3 = random.choice(resimler_listesi3)
    with open(f'images3/{rastgele_resim3}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)





@bot.command()
async def uzayli(ctx):
    resimler_listesi = os.listdir("images")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'uzayli/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

bot.run("TOKEN")
