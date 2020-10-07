import os
import random
from imdb import IMDb
from dotenv import load_dotenv
from discord.ext import commands
from PIL import Image
import urllib.request
import discord.file
from time import sleep

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='-')
ia = IMDb()


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server'
    )


@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name='roll', help='Simulates rolling dice.')
async def roll(ctx, number_of_sides: int = 6, number_of_dice: int = 1):
    if number_of_sides > 100 or number_of_sides < 1 or number_of_dice > 10 or number_of_dice < 0:
        message = "Invalid number"

    else:
        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)]
        message = ', '.join(dice)
    await ctx.send(message)


@bot.command(name="imdbs")
async def search_movie(ctx, *movie):
    movie = " ".join(movie)
    movies = ia.search_movie(movie)
    top_result = ia.get_movie(movies[0].getID())

    title, genres, rating = get_title_rating_genre(top_result)

    await ctx.send(f"Title: {title}\n"
                   f"Rating: {rating}\n"
                   f"Genre: {genres}\n"
                   f"{ia.get_imdbURL(top_result)}"
                   )


@bot.command(name="ugøy")
async def play_ugøy(ctx):
    # Gets voice channel of message author
    vc = await ctx.message.author.voice.channel.connect()

    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('ugy_jon.mp3'), after=lambda e: print('done', e))

    while vc.is_playing():
        sleep(.1)

    await vc.disconnect()

    await ctx.message.delete()


def get_title_rating_genre(movie):
    try:
        title = movie['title']
    except KeyError:
        title = "*No title available*"

    try:
        genres = ", ".join(movie['genre'])
    except KeyError:
        genres = "*No genre available*"

    try:
        rating = movie['rating']
    except KeyError:
        rating = "*No rating available*"

    return title, genres, rating


def create_temp_cover_file(coverurl):
    with urllib.request.urlopen(coverurl) as url:
        with open('temp.jpg', 'wb') as f:
            f.write(url.read())
            f.close()


bot.run(TOKEN)
