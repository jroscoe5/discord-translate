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
        await self.change_presence(activity=discord.Game('jonnie is my daddy'))

    async def on_message(self, msg):
        # Doesn't respond to itself if something like "t!en t!en loop" is said
        if msg.author == self.user:
            return
        try:
            # backdoor for status changes
            if msg.channel.id == 531761211067465728 and msg.content.split(' ')[0] == 't!status':
                await self.change_presence(activity=discord.Game(msg.content[7:]))
                return

            self.logger.log_msg(msg)
            res = self.parse_msg(msg)

            if not res['success']:
                return

            trans = self.translate(content=res['text'], lang=res['lang'])
            res['trans'] = trans
            self.logger.log_trans(res)

            await msg.channel.send(trans)
        except Exception as exc:
            self.logger.log_exc(exc)

    def translate(self, content, lang):
        return self.translator.translate(text=content,dest=lang).text

    def parse_msg(self, msg):
        result = {'success':False, 'lang':'', 'text':'', 'trans':''}
        content = msg.content

        # Check if msg starts with prefix
        if len(content) < 2 or content[:2] != self.prefix:
            return result

        splitContent = content.split(' ')

        # Check if message contains more than prefix
        if len(splitContent) < 2:
            return result

        # Destination language should directly follow tag (default is English)
        result['lang'] = 'en'
        if len(splitContent[0]) > 2:
            result['lang'] = splitContent[0][2:]

        # Remainder of message should be translated
        result['text'] = content[len(splitContent[0]):]
        result['success'] = True
        
        return result
