# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 10:49:42 2022

@author: Mitchell
"""

import nest_asyncio
nest_asyncio.apply()

import asyncio, discord
from discord.ext import commands

ffmpeg_options = {'options': '-vn'}


def SESource(x):
    return "".join(['File path for local mp3s', str(x),'.mp3'])

class Sound_Effect(commands.Cog):
    def __init__self(self, bot):
        self.bot = bot
    
    
    @commands.command()
    async def options(self, ctx):
        """Gives bot Documentation"""
        #channel = bot.get_channel(#########)
        await ctx.author.send('Message to be sent on ~options call')
    
    
    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""
        
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        
        await channel.connect()
            
    @commands.command()
    @commands.cooldown(1,10,commands.BucketType.guild)
    async def play(self, ctx, *, query):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(SESource(query)))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

        #await ctx.send('Now playing: {}'.format(query))
        

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.guild)
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send("Changed volume to {}%".format(volume))

    @commands.command()
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()

    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()
    
    
bot = commands.Bot(command_prefix=commands.when_mentioned_or('~'),description='Emote Bot')

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')
    await bot.get_channel(channel).send('Send a login message to a specified channel')

bot.add_cog(Sound_Effect(bot))
    
bot.run(token)