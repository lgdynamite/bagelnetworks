### teams Bot ###
from webexteamsbot import TeamsBot
from webexteamsbot.models import Response

# RESTCONF Setup
port = '443'
url_base = "https://{h}/restconf".format(h=device_address)
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

# Bot Details
bot_email = 'AuvikBagelBot@webex.bot'
teams_token = 'NGVmZDc2ZDctOGU3Ny00Njk1LWFlZTQtNmVhYWIxZjBhZjc1MGMxZGY2ZWQtNmM4_P0A1_d5fe8096-9b9a-43dd-bc72-9f86104a819b'
bot_url = "https://webex-auvik-python.azurewebsites.net/"
bot_app_name = 'Auvik Bagel Bot'

# Create a Bot Object
#   Note: debug mode prints out more details about processing to terminal
bot = TeamsBot(
    bot_app_name,
    teams_bot_token=teams_token,
    teams_bot_url=bot_url,
    teams_bot_email=bot_email,
    debug=True,
    webhook_resource_event=[
        {"resource": "messages", "event": "created"},
        {"resource": "attachmentActions", "event": "created"},],
)

# Create a function to respond to messages that lack any specific command
# The greeting will be friendly and suggest how folks can get started.
def greeting(incoming_msg):
    # Loopkup details about sender
    sender = bot.teams.people.get(incoming_msg.personId)

    # Create a Response object and craft a reply in Markdown.
    response = Response()
    response.markdown = "Hello {}, I'm a friendly CSR1100v assistant .  ".format(
        sender.firstName
    )
    response.markdown += "\n\nSee what I can do by asking for **/help**."
    return response
