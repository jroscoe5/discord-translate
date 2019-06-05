from os import sys
from translatorbot import TranslatorBot
import logger

token = open('token\\token.dtoken').readline()
bot = TranslatorBot(logger.Logger(sys.stdout, logger.Verbosity.high))
bot.run(token)