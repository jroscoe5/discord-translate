# python 3.7.1

import discord

class TranslatorBot(discord.Client):

    def __init__(self, logger):
        super().__init__()
        self.logger = logger

    async def on_ready(self):
        self.logger.log('Connection established')
        self.logger.log('Connected as: ' + str(self.user))
        self.user.activity = discord.Game(name='with itself')

    async def on_message(self, msg):
        pass
