import discord
import random

import config


class MyBot(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        commands = ["who be juan olek", "who be juan enri", "who be juan help", "who be juan"]
        responses = [f"Olha {message.author.name} sobes ao {random.randint(0,1000)}º andar e saltas.",
                     "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngwing.com%2Fpt%2Ffree-png-nvdjt&psig=AOvVaw1X2eir3P_6rFufQriGXwCJ&ust=1639070346208000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCNjt4__a1PQCFQAAAAAdAAAAABAD",
                     "who be juan kanobi"]
        if message.content == commands[0]:
            await message.channel.send(responses[0])
        elif message.content == commands[1]:
            await message.channel.send(responses[1])
        elif message.content == commands[2]:
            response = "\n".join(commands)
            await message.channel.send(response)
        elif message.content == commands[3]:
            await message.channel.send(responses[2])
        if "jura" in message.content:
            await message.channel.send("JUROOOO")
        if "hum" in message.content and not (message.author == self.user):
            await message.channel.send("hum")

    async def on_member_join(self, member):
        print("here")
        guild = member.guild
        print(guild)
        if guild.system_channel is not None:
            message = f"Olha quem é ele/a!!!\n Parece que o/a {member.name} decidiu aparecer."
            print(message)
            await guild.system_channel.send(message)


intents = discord.Intents.default()
intents.members = True
client = MyBot(intents=intents)
#must have a file named config.py and have a fiels name token with the token to work
client.run(config.token)
