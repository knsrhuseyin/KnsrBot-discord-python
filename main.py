import discord
from discord import *
from tokenBot import *


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        game = discord.Game("Test")
        await self.change_presence(status=discord.Status.idle, activity=game)

    async def on_message(self, message_content):
        if message_content.author.id == self.user.id:
            return

        if message_content.content.startswith("Hello"):
            await message_content.channel.send("Hello !")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(tokenBot)
