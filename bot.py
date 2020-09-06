# bot.py

import discord
import json
import datetime
from threading import Timer


tokenReader = open("token.txt", "r")
token = tokenReader.read()




client = discord.Client()
@client.event
async def on_ready():
	print('Logged in as {0.user}'.format(client))
	# client.loop.create_task(checkTime())


egging = False
prefix = '!'
approved_egging_words = ['egg', 'huevo', 'tamago', 'たまご', '卵']
eggChannel = None

def deltaEgg():
	global egging
	egging = False
	print("Egg stopped")
	
	
@client.event
async def on_message(message):
	global egging, prefix, approved_egging_words, eggChannel
	if message.author == client.user:
		return
	
	msg = message.content
	if msg[:len(prefix)] != prefix or len(msg) <= len(prefix):
		return
	msg = msg[1:]
	msg = msg.split(' ')
	
	if msg[0] in approved_egging_words:
		if egging:
			return
		if eggChannel == None:
			await message.channel.send("Egg channel has not been set up! Use `" + prefix + "setChannel` to set up")
			return
		# elif len(message.author.voice.channel) >= 2:
		mav = message.author.voice
		if mav != None:
			if len(mav.channel.members) >= 2:
				egging = True
				t = Timer(10.0, deltaEgg)
				t.start()
				print(message.author.display_name + " started a " + msg[0] + ".") 
	elif msg[0] == "setChannel":
		eggChannel = message.channel.id
		await message.channel.send("Egg channel set!")


@client.event
async def on_voice_state_update(member, before, after):
	global egging, members_in_vc, eggChannel
	if egging:
		if after.channel == None:
			channelPeople = before.channel.members
			if len(channelPeople) == 1:
				channel = client.get_channel(eggChannel)
				await channel.send("{} egg" .format(channelPeople[0].mention)) 
				egging = False



	
client.run(token)