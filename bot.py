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

@client.event
async def on_message(message):
	global egging, prefix, approved_egging_words
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
		# elif len(message.author.voice.channel) >= 2:
		mav = message.author.voice
		if mav != None:
			if len(mav.channel.members) >= 2:
				egging = True
                t = Timer(10.0, lambda: egging = False)
                t.start()
				print(message.author.display_name + " started un huevo.")


@client.event
async def on_voice_state_update(member, before, after):
	global egging, members_in_vc 
	if egging:
		if after.channel == None:
			channelPeople = before.channel.members
			if len(channelPeople) == 1:
				channel = client.get_channel(671538516005748750)
				await channel.send("{} egg" .format(channelPeople[0].mention)) 
				egging = False



	
client.run(token)