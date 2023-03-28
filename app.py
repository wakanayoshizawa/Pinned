# coding: utf-8

import os
import discord

TOKEN = os.environ.get('DISCORD_BOT_TOKEN')

client = discord.Client()

"""
起動イベント
"""
@client.event
async def on_ready():
    print('BOT起動')

"""
リアクションイベント
"""
@client.event
async def on_raw_reaction_add(payload):

    if payload.emoji.name == '📌':
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        await message.pin()
        return

@client.event
async def on_raw_reaction_remove(payload):

    if payload.emoji.name == '📌':
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        await message.unpin()
        return

client.run(TOKEN)