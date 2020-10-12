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


@bot.command(name="disconnectvc")
async def leave_vc(ctx):
    vc = get_voice_channel_bot(ctx)
    if vc:
        await vc.disconnect()

@bot.command(name="ugøy")
async def play_ugøy(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('ugy_jon.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()

@bot.command(name="spela")
async def play_ugøy(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('spela.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()

@bot.command(name="start")
async def play_ugøy(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('start.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="drid")
async def play_ugøy(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('drid.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()



@bot.command(name="sikkert")
async def play_ugøy(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('sikkert.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()

@bot.command(name="sikkert2")
async def play_ugøy(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('sikkert2.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()

@bot.command(name="ai")
async def play_ai(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('ai.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()

@bot.command(name="aaah")
async def play_ape(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('aaah.m4a'), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="gjesp")
async def play_gjesp(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('gjesp.m4a'), after=lambda e: print('done', e))

    await ctx.message.delete()

@bot.command(name="ape2")
async def play_ape2(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('ape2.m4a'), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="stivi")
async def play_stivi(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('stivi.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()

@bot.command(name="marengs")
async def play_marengs(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('marengs.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="kjeften")
async def play_hold_kjeft(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('holdkjeft.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="sur")
async def play_ape(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('sur.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="grim")
async def play_grim(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('grim.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()




@bot.command(name="åå")
async def play_ååå(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('ååå.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()



@bot.command(name="mhm")
async def play_ååå(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('mhm.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="sikkje")
async def play_ååå(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('sikkje.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()



@bot.command(name="nice")
async def play_ååå(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('nice.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="degseie")
async def play_ååå(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('degseie.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="gidde")
async def play_ååå(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('gidde.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="ragev")
async def play_ååå(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('ragev.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="ins")
async def play_ååå(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('ins.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="stikke")
async def play_stikke(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('stikkeeg.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="samev")
async def play_samev(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('samev.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="sisisi")
async def play_samev(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('sisisi.m4a'), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="gjespj")
async def play_gjespj(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('gjespj.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="stikkej")
async def play_stikkej(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('stikkejl.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="ape")
async def play_ape(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('ape.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()

@bot.command(name="brann")
async def play_brann(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('brann.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()

@bot.command(name="dildo")
async def play_dildo(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('dildo.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()

@bot.command(name="dildo2")
async def play_dildo(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('dildo2.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()

@bot.command(name="ser")
async def play_dildo(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('ser.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()

@bot.command(name="rc")
async def play_dildo(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('rc.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="hallo")
async def play_dildo(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('hallo.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()

@bot.command(name="tfm")
async def play_tfm(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('tfm.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="vann")
async def play_vann(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('vann.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()



@bot.command(name="same")
async def play_same(ctx):
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

    print(is_connected(ctx))

    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('same.mp3'), after=lambda e: print('done', e))

    await ctx.message.delete()


@bot.command(name="yomama")
async def search_movie(ctx):
    jokes = {}
    with open('yomamajokes.txt') as f:
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


@bot.command(name="rage")
async def play_rage(ctx):
    # Gets voice channel of message author
    voice_channel = get_voice_channel_author(ctx)
    if not voice_channel:
        return

    if ctx.voice_client is None:
        vc = await voice_channel.connect()
    else:
        await ctx.voice_client.move_to(voice_channel)
        vc = ctx.voice_client
    print(is_connected(ctx))
    if not is_connected(ctx):
        vc = await ctx.message.author.voice.channel.connect()

    sleep(0.2)
    # Requires that FFmpeg (and frei0r-plugins (?)) is installed on host machine
    vc.play(discord.FFmpegPCMAudio('ragel.mp3'), after=lambda e: print('done', e))

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
