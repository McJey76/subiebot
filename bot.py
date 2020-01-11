import discord
from discord.ext    import commands
from discord.ext.commands   import Bot
import asyncio
 
bot = commands.Bot(command_prefix='#')
 
@bot.event
async def on_ready():
    print ("Ready to send rods to space!")
 
 
@bot.event
async def on_message(message):
    if(message.channel.id == "600512635519369236"):
        await bot.add_reaction(message, "⭐")
 
 
bot.run("NjA0MDQxMzc5NDgzNDg0MTYw.XhlSfQ.DyMiswWhggXjNVpmbHrmMiH0Gu8")