import discord
from discord.ext import commands
import asyncio

my_token = 'NTAzNDQyMTI3NjI0MjA4Mzk1.Dq26xg.j7_57wgIbB3Z8nPtyRwWS1_Kv3A'

bot=commands.Bot(command_prefix='D!')

@bot.event
async def on_ready():
	print('The bot is ready!')
	print(bot.user.name)
	print(bot.user.id)
	print('----------------------------')

@bot.command()
async def touch():
	await bot.say('im gonna touch this')
@bot.command()
async def oof():
	await bot.say('hello')

@bot.command()
async def hey():
	await bot.say('wassuh')

@bot.command()
async def hot():
	await bot.say('lil pinaple')
	await bot.say('Dont try it.. You dont have any chance. Heheh')	
		
bot.run(my_token)
