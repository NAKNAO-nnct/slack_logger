from slackbot.bot import *
import re

@default_reply
def my_default_handler(message):
    print(message.body)
    message.reply('...')

@listen_to('', re.IGNORECASE)
def help(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply('Yes, I can!')

    # Message is sent on the channel
    message.send('I can help everybody!')

    # Start a thread on the original message
    message.reply("Here's a threaded reply", in_thread=True)