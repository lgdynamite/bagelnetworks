from webex_bot.webex_bot import WebexBot
from gpt import gpt

bot = WebexBot("NGVmZDc2ZDctOGU3Ny00Njk1LWFlZTQtNmVhYWIxZjBhZjc1MGMxZGY2ZWQtNmM4_P0A1_d5fe8096-9b9a-43dd-bc72-9f86104a819b")
bot.commands.clear()
bot.add_command(gpt())
bot.help_command = gpt()
bot.run()
