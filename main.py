
import random
import discord
import os
from discord.ext import tasks
from discord.ext.commands import Bot
from discord.ext.commands import AutoShardedBot
import time

y = ["1", "2" ,"3", "4", "5", "6"]

bot = Bot(command_prefix="/")


bot = AutoShardedBot(command_prefix="/")
@bot.command(name="hex")
async def send_message(ctx):
  c = bot.get_channel(937579766784065598) or (await bot.fetch_channel(937579766784065598))
  await ctx.send(hex(random.randint(1, 999999999999999999999999999999999999999999))) #Hexadecimal generate

@bot.command(name="random")
async def random_cmd(ctx):
  c = bot.get_channel(937563323254321183) or (await bot.fetch_channel(937563323254321183)) #Random dice roll 
  await ctx.send(f"You have rolled a {random.randint(1, 11)}")

@bot.command(name="hello")
async def send_message():
  c = bot.get_channel(929149843283275816) or (await bot.fetch_channel(929149843283275816)) #Hello Command
  await ctx.send("Hello there!")

bot.run("token")



