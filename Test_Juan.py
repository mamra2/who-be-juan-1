import discord
import random
import pyjokes
import cowsay
import youtube_dl
from discord import client
from google_translator_simplified import Translator

import config
import Lists
import commands


class MyBot(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        channel = discord.utils.get(client.get_all_channels(), name="general")
        await client.get_channel(channel.id).send("Ahhh shit here we go again...")

    async def on_message(self, message):

        responses = Lists.Responses(message)
        commands_list = commands.commands

        if message.content == commands_list[0]:
            await message.channel.send(responses.responses_olek[0])

        elif message.content == commands_list[1]:
            number = random.randint(0, len(responses.responses_enri) - 1)
            await message.channel.send(responses.responses_enri[number])

        elif message.content == commands_list[2]:
            response = "\n".join(commands_list)
            await message.channel.send(response)

        elif message.content == commands_list[3]:
            await message.channel.send(responses.responses[0])

        elif message.content == commands_list[4] or message.content == commands_list[5]:
            number = random.randint(1, len(responses.responses_olek) - 1)
            await message.channel.send(responses.responses_olek[number])

        elif message.content == commands_list[6]:
            await message.channel.send(pyjokes.get_joke(category="all"))

        elif message.content == commands_list[7]:
            number = random.randint(0, len(responses.responses_negro) - 1)
            await message.channel.send(responses.responses_negro[number])

        elif commands_list[8] in message.content and message.author != self.user:
            if message.content[17:] != "":
                await message.channel.send(message.content[17:])

            number = random.randint(0, len(responses.responses_kill) - 1)
            a = "```" + cowsay.get_output_string("cow", f"{responses.responses_kill[number]}") + "```"
            await message.channel.send(a)

        elif message.content == commands_list[9]:
            number = random.randint(1, len(responses.responses) - 1)
            a = f"""```
                                            ═▂▄▄▓▄▄▂
                                ◢◤ █▀▀████▄▄▄▄◢◤
                                █▄ █ █▄ ███▀▀▀▀▀▀▀╬
                                ◥█████◤
                                ══╩══╩═
                                ╬═╬
                                ╬═╬ just dropped down to say
                                ╬═╬
                                ╬═╬ You’re hella {responses.responses[number]}
                                ╬═╬☻/
                                ╬═╬/▌
                                ╬═╬/ l
                                            ```"""
            await message.channel.send(a)

            """
            NAO MEXER... NAO ME PERGUNTEM PK MAS FUNCIONA
            """

        elif message.content == commands_list[10]:
            number = random.randint(0, len(responses.responses_flirt)-1)
            await message.channel.send(responses.responses_flirt[number])

        elif message.content.startswith(commands_list[11]):
            translate = message.content[22:]
            detected_language = Translator.detect_lang(translate)
            await message.channel.send(Translator.get_translation('pt', translate, detected_language))


        elif message.content.startswith(commands.commands_music[0]):
            if message.author.voice is None:
                await message.channel.send("Please join a voice channel to use this command")
            else:
                channel1 = message.author.voice.channel
                global voice_client
                voice_client = await channel1.connect()

        elif message.content.startswith(commands.commands_music[1]):
            if message.author.voice is None:
                await message.channel.send("Please join a voice channel to use this command")
            else:
                await voice_client.disconnect()

                """
                NAO MEXER... NAO ME PERGUNTEM PK MAS FUNCIONA
                """

        elif message.content.startswith(commands.commands_music[2]):
            FFMPEG_OPTIONS = {'before_option': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                              'options': '-vn'}
            YDL_OPTIONS = {'format': 'bestaudio/best'}
            vc = voice_client
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                print(message.content[17:])
                info = ydl.extract_info(message.content[17:], download=False)
                url2 = info['formats'][0]['url']
                print(url2)
                source = await discord.FFmpegPCMAudio(executable="ffmpeg", source=url2)
                vc.play(source)

        if "jura" in message.content:
            await message.channel.send("JUROOOO")

        if any(response in message.content for response in responses.responses_censured) and not (message.author == self.user):
            number = random.randint(0,len(responses.responses_cen)-1)
            await message.channel.send(responses.responses_cen[number])

        if "wtf" in message.content:
            await message.channel.send("Tem calma colega")

        if "NAO" in message.content:
            await message.channel.send("SIMMMMM")

        if any(response in message.content for response in responses.responses_explanations):
            await message.channel.send("explaainnn")

        if "??" in message.content and not (message.author == self.user):
            await message.channel.send("??")

        if "hum" in message.content and not (message.author == self.user):
            await message.channel.send("hum")

        if "nice" in message.content and "mega" not in message.content and not (message.author == self.user):
            await message.channel.send("69")

        if "69" in message.content and not (message.author == self.user):
            await message.channel.send("nice")

        if "mega nice" in message.content:
            await message.channel.send("42069")

        if "imagina" in message.content and not (message.author == self.user):
            await message.channel.send("Mas imagina mesmo!!")

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            message = f"Olha quem é ele!!!\nParece que o {member.mention} decidiu aparecer."
            await guild.system_channel.send(message)


intents = discord.Intents.default()
intents.members = True
client = MyBot(intents=intents)
# must have a file named config.py and have a field name token with the token to work
client.run(config.token)
