import discord
from discord import *


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        game = discord.Game("Test")
        await client.change_presence(status=discord.Status.idle, activity=game)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('ODE3MTc2OTc5MzIwNzMzNzM0.GyjLn6.hOuJ-EAdSD2_8ifdMVBRznye715BjiObpkj6LM')
