import discord
import random

import config


class MyBot(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        commands = ["who be juan olek", "who be juan enri", "who be juan help", "who be juan", "who be juan trabalho"]
        responses = [f"Olha {message.author.name} sobes ao {random.randint(0,1000)}º andar e saltas.",
                     "https://w7.pngwing.com/pngs/837/520/png-transparent-a-monkey-s-orientation-chimpanzee-cymbal-banging-monkey-toy-monkey-animals-snout-cymbal-thumbnail.png",
                     "who be juan kanobi",
                     "Isso dá muito trabalho..."]
        if message.content == commands[0]:
            await message.channel.send(responses[0])
        elif message.content == commands[1]:
            await message.channel.send(responses[1])
        elif message.content == commands[2]:
            response = "\n".join(commands)
            await message.channel.send(response)
        elif message.content == commands[3]:
            await message.channel.send(responses[2])
        elif message.content == commands[4]:
            await message.channel.send(responses[3])
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
# must have a file named config.py and have a fiels name token with the token to work
client.run(config.token)
