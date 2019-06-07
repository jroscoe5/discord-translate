# python 3.7.1

from os import sys, environ
from translatorbot import TranslatorBot
import logger

token = environ['token']
bot = TranslatorBot(logger.Logger(sys.stdout, logger.Verbosity.none))
bot.run(token)