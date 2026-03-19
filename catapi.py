import os
from dotenv import load_dotenv
import discord
import psutil
from responses import responses
from discord.ext import commands
import traceback

intents = discord.Intents.default()
intents.message_content = True
load_dotenv()
client = discord.Client(intents=intents)
TOKEN = os.getenv("DISCORD_TOKEN")
COUNTER_ID = int(os.getenv("COUNT_CHANNEL_ID"))
WRIJU = int(os.getenv("WRIJU_ID"))
STATUS_FILE = "/home/thecataclysmo/discordbot/bot_status.txt"
bot = commands.Bot(command_prefix='$', intents=intents)
@client.event
async def on_ready():
    with open(STATUS_FILE, "w") as f:
         f.write("online")
    print(f'Logged in as {client.user}')

@client.event
async def on_resumed():
    with open(STATUS_FILE, "w") as f:
         f.write("online")
    print('Resumed connection')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    content = message.content.lower()    
    for trigger, reply in responses.items():
            if content.startswith(trigger):

                        if callable(reply):
                              reply = reply(message)

                        await message.channel.send(reply)
                        return
    if message.channel.id == COUNTER_ID:
        if content:
            first_word = content.split()[0]
            if first_word.isdigit():
                number = int(first_word) + 1
                await message.channel.send(str(number))
                return
    elif message.author.id == WRIJU:
        await message.channel.send ("loln't")
    elif message.content.startswith('$stat'):
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        cpu = psutil.cpu_percent(interval=1)
        mem_used = mem.used / (1024**2)
        mem_total = mem.total / (1024**2)

        disk_used = disk.used / (1024**3)
        disk_total = disk.total / (1024**3)

        stats = (f"CPU: {cpu}%\n"
                 f"RAM: {mem_used:.1f}MB / {mem_total:.1f}MB\n"
                 f"DISK: {disk_used:.1f}GB / {disk_total:.1f}GB")
        await message.channel.send(stats)
@client.event
async def on_disconnect():
     with open(STATUS_FILE, "w") as f:
          f.write("offline")
@client.event
async def on_error(event, *args, **kwargs):
    print("Error in event:", event)
    traceback.print_exc()

@bot.command()
async def test(ctx, arg):
     await ctx.send(arg)

bot.add_command(test)    
client.run(TOKEN)        

