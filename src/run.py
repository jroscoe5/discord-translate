# python 3.7.1

from os import sys
from translatorbot import TranslatorBot
import logger

token = open('token/token.dtoken').readline()
bot = TranslatorBot(logger.Logger(sys.stdout, logger.Verbosity.none))
bot.run(token)
