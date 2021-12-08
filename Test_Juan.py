import discord
import random

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
            await message.channel.send(responses.get_responses_olek(0))

        elif message.content == commands_list[1]:
            number = random.randint(0, 1)
            await message.channel.send(responses.get_responses_enri(number))

        elif message.content == commands_list[2]:
            response = "\n".join(commands_list)
            await message.channel.send(response)

        elif message.content == commands_list[3]:
            await message.channel.send(responses.get_response(0))

        elif message.content == commands_list[4] or message.content == commands_list[5]:
            number = random.randint(1, 3)
            await message.channel.send(responses.get_responses_olek(number))

        if "jura" in message.content:
            await message.channel.send("JUROOOO")

        if "hum" in message.content and not (message.author == self.user):
            await message.channel.send("hum")
        if "nice" in message.content and "mega" not in message.content and not (message.author == self.user):
            await message.channel.send("69")
        if "69" in message.content and not (message.author == self.user):
            await message.channel.send("nice")
        if "mega nice" in message.content:
            await message.channel.send("42069")

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            message = f"Olha quem é ele/a!!!\n Parece que o/a {member.name} decidiu aparecer."
            await guild.system_channel.send(message)


intents = discord.Intents.default()
intents.members = True
client = MyBot(intents=intents)
# must have a file named config.py and have a field name token with the token to work
client.run(config.token)
