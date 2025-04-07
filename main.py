import nest_asyncio, os, asyncio, discord
from discord.ext import commands
from dotenv import load_dotenv
import logging

nest_asyncio.apply()

load_dotenv()

test_server_id = int(os.getenv('TEST_SERVER_ID'))
main_server_id = int(os.getenv('DISCORD_SERVER_ID'))
application_id = int(os.getenv('APPLICATION_ID'))
public_key = os.getenv('PUBLIC_KEY')
client_id = int(os.getenv('CLIENT_ID'))
token = os.getenv('TOKEN')
dropbox_url = os.getenv('DROPBOX_URL')
direct_mp3_3am = os.getenv('DIRECT_MP3_3AM')
test_server_text_channel = int(os.getenv('TEST_SERVER_CHANNEL_ID'))
main_server_text_channel = int(os.getenv('MAIN_SERVER_CHANNEL_ID'))


ffmpeg_options = {'options': '-vn'}

intents = discord.Intents.all()
    
mainBot = commands.Bot(command_prefix=commands.when_mentioned_or('~'),description='Emote Bot', intents=intents)

@mainBot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(mainBot.user))
    print('------')
    await mainBot.get_channel(test_server_text_channel).send('Send a login message to a specified channel')


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await mainBot.load_extension(f"cogs.{filename[:-3]}")

handler = logging.FileHandler(filename='discord.log',encoding='utf-8',mode='w')

async def main():
    async with mainBot:
        await load_extensions()
        await mainBot.run(token, log_handler=handler, log_level=logging.DEBUG)



asyncio.run(main())