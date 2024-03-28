### teams Bot ###
from webexteamsbot import TeamsBot
from webexteamsbot.models import Response
### Utilities Libraries
import routers
import useless_skills as useless
import useful_skills as useful

# Router Info 
device_address = routers.router['host']
device_username = routers.router['username']
device_password = routers.router['password']

# RESTCONF Setup
port = '443'
url_base = "https://{h}/restconf".format(h=device_address)
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

# Bot Details
bot_email = '381Bot@webex.bot'
teams_token = 'MmUwYjBiZjctODlkNC00MzVhLTk5NWQtMGQxNzY2M2EwZjI2MzlkNGI1YTAtNWM3_P0A1_5d96674f-de50-43d7-ae6b-8071b71cb457'
bot_url = "https://0c52-66-188-237-165.ngrok.io"
bot_app_name = 'CNIT-381 Network Auto Chat Bot'

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
