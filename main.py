from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response 

# loading the token from .env file
load_dotenv('.env')

TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# setting up bot
intents: Intents = Intents.default()
intents.message_content = True 
client: Client = Client(intents=intents)

