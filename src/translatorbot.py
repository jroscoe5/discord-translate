# python 3.7.1

import discord
from googletrans import Translator

class TranslatorBot(discord.Client):

    def __init__(self, logger):
        super().__init__()
        self.logger = logger
        self.prefix = 't!'
        self.translator = Translator()

    async def on_ready(self):
        self.logger.log('Connection established')
        self.logger.log('Connected as: ' + str(self.user))
        await self.change_presence(activity=discord.Game('documentation link coming in the future'))

    async def on_message(self, msg):
        if msg.author == self.user:
            return

        self.logger.logMsg(msg)
        content = msg.content

        if len(content) < 6: 
            return

        tag = content.split(' ')[0]
        if tag[:2] != self.prefix:
            return
        try:
            text = content[len(tag):]
            result = self.translate(text, dest=tag[2:])
            self.logger.log('Translated: ' + result)
            await msg.channel.send(result)
        except Exception as exc:
            self.logger.log(exc)

    def translate(self, content, dest):
        return self.translator.translate(text=content,dest=dest).text
        
