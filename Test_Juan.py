import discord
import random

import config


class MyBot(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        commands = ["who be juan olek", "who be juan enri", "who be juan help", "who be juan", "who be juan trabalho", "who be juan trabalha"]
        responses = [f"Olha {message.author.name} sobes ao {random.randint(0,1000)}º andar e saltas.",
                     "https://c.tenor.com/lVLSSglhk1cAAAAC/monkey-cymbals.gif", "https://c.tenor.com/7Glf51FDQZQAAAAM/monkey-annoying.gif",
                     "who be juan kanobi",
                     "Isso dá muito trabalho...", "@rogue#0001 faz tu!", "https://media1.tenor.com/images/5ad50b6db3dc7ed4ca10dd65d4ea84c2/tenor.gif?itemid=11811769"]
        if message.content == commands[0]:
            await message.channel.send(responses[0])
        elif message.content == commands[1]:
            number = random.randint(1, 2)
            await message.channel.send(responses[number])
        elif message.content == commands[2]:
            response = "\n".join(commands)
            await message.channel.send(response)
        elif message.content == commands[3]:
            await message.channel.send(responses[2])
        elif message.content == commands[4] or message.content == commands[5]:
            number = random.randint(4, 6)
            await message.channel.send(responses[number])
        if "jura" in message.content:
            await message.channel.send("JUROOOO")
        if "hum" in message.content and not (message.author == self.user):
            await message.channel.send("hum")

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            message = f"Olha quem é ele/a!!!\n Parece que o/a {member.name} decidiu aparecer."
            await guild.system_channel.send(message)


intents = discord.Intents.default()
intents.members = True
client = MyBot(intents=intents)
# must have a file named config.py and have a fiels name token with the token to work
client.run(config.token)
