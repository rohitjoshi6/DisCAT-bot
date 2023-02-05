import discord
from discord.ext import commands
import asyncio
import requests
import os

prefix = "!"

bot = commands.Bot(command_prefix=prefix, self_bot=False, bot=True, intents=discord.Intents.all())


@bot.event
async def on_ready():
    change_status.start()
    print('Logged in as')
    print(self.user.name)
    print(self.user.id)

activity = ["online", "idle", "dontd"]
status = ["Yoo!",
         prefix+"cat"]

@tasks.loop(seconds=10)
async def change_status():
    # it may work without `global` but I am not sure
    global status, activity
    botStats = random.randint(0, len(status) - 1)
    activityStats = random.randint(0, len(activity) - 1)
    if activity[activityStats] == "online":
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=status[botStats]))
    elif activity[activityStats] == "idle":
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=status[botStats]))
    else:
        await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name=status[botStats]))
        
        
    
@bot.command()
async def cat(ctx):
    if message.author == self.user:
        return
            
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    await message.channel.send(data['file'])
    
    


token = "Your discord bot token here"
bot.run(token)
