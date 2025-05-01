import discord
import os
import logging
from dotenv import load_dotenv
from commands import handle_command
from datetime import datetime

# LOG CONFIG
os.makedirs("logs", exist_ok=True)
log_file = f"logs/log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

# INIT
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logging.info(f'Logada como {client.user} UwU')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await handle_command(client, message)

client.run(DISCORD_TOKEN)
