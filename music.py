import discord
from discord.ext import commands
from youtube_dl import YoutubeDL


class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="join", help="you must be in a voice channel")
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Please join a voice channel to use this command")
            return
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command(name="leave", help="the bot must be in a voice channel")
    async def leave(self, ctx):
        try:
            await ctx.voice_client.disconnect()
        except:
            await ctx.send("Ain't even there bruh")

    # TODO tentar ver se isto da... senao usar igual ao que o henrique tem e dps vê-se os opus
    @commands.command(name="play", help="who be juan play <youtube url>")
    async def play(self, ctx, url):
        vc = ctx.voice_client
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                          'options': '-vn'}

        if not vc.is_playing():
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                URL = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(URL, **FFMPEG_OPTIONS)
                vc.play(source)
                vc.is_playing()

    @commands.command(name="stop", help="the bot must be playing")
    async def stop(self, ctx):
        vc = ctx.voice_client
        try:
            if vc.is_playing():
                vc.stop()
                await ctx.send("A'igh, imma headout. But I'm taking this beat with me")
        except:
            await ctx.send("Ain't even playing bruh")

    @commands.command(name="pause", help="the bot must be playing")
    async def pause(self, ctx):
        vc = ctx.voice_client
        try:
            if vc.is_playing():
                vc.pause()
                await ctx.send("Bruh, you really paused me to talk trash? SMH")
        except:
            await ctx.send("Ain't even playing bruh")

    @commands.command(name="resume", help="the bot must be paused")
    async def resume(self, ctx):
        vc = ctx.voice_client
        try:
            if not vc.is_playing():
                vc.resume()
                await ctx.send("Man, shut yo ass. Imma just resume this beat")
        except:
            await ctx.send("Não mandas em mim!")


def setup(client):
    client.add_cog(music(client))
