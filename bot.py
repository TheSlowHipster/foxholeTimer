import json
import logging
import time
import discord
from discord.ext import commands, tasks

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='UTF-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))

with open(config.json) as f:
    config = json.load(f)
    f.close()

description = ''' A timer to remind users after a set period of time.

written by @TheSlowHipster https://github.com/TheSlowHipster
'''

intents = discord.Intents.default()

bot = commands.Bot(command_prefix=config["prefix"], description=description, intents=intents)

guild = None
channel = None

@bot.event
async def on_ready():
    hasChannel = False
    for gui in bot.guilds:
        for chan in tmp.channels:
            if chan.name == config['channelName']:
                channel = chan
                hasChannel = True
                break
        if hasChannel:
            guild = gui
            break

@tasks.loop(hours=48)
async def timer(self):
    if guild is None or channel is None:
        print("No guild or channel")
        return
    await time.sleep(162000) # Sleep for 45 hours
    await channel.send(f"<&@{config['roleID']}> stockpiles will expire in approximately 3 hours.")
    await time.sleep(3600)
    await channel.send(f"<&@{config['roleID']}> stockpiles will expire in approximately 2 hours.")
    await time.sleep(3600)
    await channel.send(f"<&@{config['roleID']}> stockpiles will expire inapproximately 1 hour."
            "This is your last reminder")



@bot.command(description ="Re-set the stockpile timer")
async def reset(ctx):
    if not timer.is_running():
        ctx.send(f"Thanks {ctx.author.name} for setting the timer!")
        timer.start()
    else:
        ctx.send(f"Thanks {ctx.author.name} for re-setting the timer!")
        timer.restart()
