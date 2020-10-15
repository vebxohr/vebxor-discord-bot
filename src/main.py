import os
import random
from imdb import IMDb
from dotenv import load_dotenv
from discord.ext import commands
from PIL import Image
import urllib.request
import discord.file
from time import sleep
from pathlib import Path
import json
from youtubesearchpython import SearchVideos
from music_player import YTDLSource

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='.')

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


@bot.command(name="play", help="Play a clip from YouTube: .play [URL]")
async def play(ctx, *url):
    if ".com" not in url and "youtube" not in url:
        search = SearchVideos(url, offset=1, mode="json", max_results=1)
        url = json.loads(search.result()).get("search_result")[0].get('link')
        print(url)
    async with ctx.typing():
        player = await YTDLSource.from_url(url, loop=bot.loop, stream=True)
        ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
    await ctx.send('Now playing: {}'.format(player.title))


@bot.command(name="pause", help="Pause the bot voice.")
async def pause(ctx):
    vc = get_voice_channel_bot(ctx)
    if vc:
        vc.pause()


@bot.command(name="resume", help="Resume the bot voice.")
async def resume(ctx):
    vc = get_voice_channel_bot(ctx)
    if vc:
        vc.resume()


@bot.command(name="stop", help="Stop the bot voice.")
async def stop_sound(ctx):
    voice_channel = get_voice_channel_bot(ctx)
    if voice_channel:
        voice_channel.stop()


@bot.command(name='roll', help='Simulates rolling dice: .roll [n sides] [n dice]')
async def roll(ctx, number_of_sides: int = 6, number_of_dice: int = 1):
    if number_of_sides > 100 or number_of_sides < 1 or number_of_dice > 10 or number_of_dice < 0:
        message = "Invalid number"

    else:
        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)]
        message = ', '.join(dice)
    await ctx.send(message)


@bot.command(name="imdbs", help="Search for a movie on IMDB: .imdbs [movie title]")
async def search_movie(ctx, *movie):
    movie = " ".join(movie)
    movies = ia.search_movie(movie)
    top_result = ia.get_movie(movies[0].getID())

    title, genres, rating = get_title_rating_genre(top_result)

    cover_url = str(top_result.get('cover url'))
    top_250_rank = top_result.get('top 250 rank')
    print(top_250_rank)


    embed = discord.Embed(
        title=title,
        description=f"**Rating:** {rating} :star:               \n"
                    f"**Genre:** {genres}\n",
        color=discord.Color.blue(),
        url=str(ia.get_imdbURL(top_result))
    )
    if top_250_rank:
        embed.description += f"**Top 250 rank:** {top_250_rank}"
    embed.set_image(url=cover_url)


    # await ctx.send(f"Title: {title}\n"
    #                f"Rating: {rating}\n"
    #                f"Genre: {genres}\n"
    #                f"{ia.get_imdbURL(top_result)}"
    #                )
    await ctx.send(embed=embed)


@bot.command(name="disconnectvc", help="Disconnect the bot from the current voice channel")
async def leave_vc(ctx):
    vc = get_voice_channel_bot(ctx)
    if vc:
        await vc.disconnect()


def get_aliases():
    f = []
    dirs = Path("../resources/")
    for file in dirs.iterdir():
        f.append(file.name.split(".")[0])
    return f


@bot.command(aliases=get_aliases(), help='Type .hsounds for commands')
async def play_sound(ctx):
    # Gets voice channel of message author
    # vc = await ctx.message.author.voice.channel.connect()

    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return

    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        vc = await voice_channel.connect()
    else:
        await ctx.voice_client.move_to(voice_channel)
        vc = ctx.voice_client

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    print("message " + ctx.message.content)
    file_name = ctx.message.content[1:] + ".mp3"
    sound_file_path = Path("../resources/") / file_name
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio(sound_file_path), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="hsounds", help="Lists available sound commands.")
async def help_sounds(ctx):
    message = str("\n".join(get_aliases()))
    message = "``` " + message + " ```"
    await ctx.send(message)


@bot.command(name="yomama", help="Get a random yo mama joke.")
async def search_movie(ctx):
    jokes = {}
    with open('../resources/yomamajokes.txt') as f:
        count = 0
        for l in f:
            jokes[count] = l
            count += 1

    number = random.choice(range(0, count))

    await ctx.send(jokes.get(number))


def is_connected(ctx):
    return ctx.voice_client and ctx.voice_client.is_connected


def get_voice_channel_author(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return None

    return ctx.author.voice.channel


def get_voice_channel_bot(ctx):
    if ctx.voice_client and ctx.voice_client.is_connected:
        return ctx.voice_client
    return None


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

