# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 21:52:07 2022

@author: Mitchell
"""

import nest_asyncio
nest_asyncio.apply()

import asyncio, discord, time
from discord.ext import commands, tasks

ffmpeg_options = {'options': '-vn'}

#permissions integer = 3147776
#Actual Seggs

ToeGremlinsServer = 989682556888817695
TestServer = 989236422831636481


def SESource(x):
    return "".join([r'/home/pi/Documents/Discord Bot Emotes/', str(x),'.mp3'])

class Sound_Effect(commands.Cog):
    def __init__self(self, bot):
        self.bot = bot
    
    
    @commands.command()
    async def options(self, ctx):
        """Gives bot Documentation"""
        #channel = bot.get_channel(#########)
        await ctx.author.send('To interact with this bot just mention me with the "@" symbol or use "~" with one of the following commands:\n\n~join - Joins a voice channel\n~volume x - Sets the volume to the integer x\n~stop - Stops and disconnects the bot from voice\n---------------------------------------------\n~play <name> - Plays the file <name> from the library below:\n\t#1 - Am I really going to deface this grave for money?\n\t3am - "Oh Boy! 3am!"\n\t4 - "Don\'t you have to be stupid somewhere else?"\n\tAdvancedDarkness - Rock Bottom\n\tAirhorn - Start your mixtape\n\tAllDay - America\'s Ass\n\tAwake - Todd Howard you son of a bitch\n\tBanjo - TWANG\n\tBarnacles - "This is a load of..."\n\tBarrage - PK\'d\n\tBathtub - No lifeguard on duty\n\tBeautiful - That hat makes you look...\n\tBeeBooBooBop - Nah man, you\'re thinking of...\n\tBelieve - Mr. Anderson\n\tBetaSonic - Thanks, Shadow.\n\tBetrayal - The Lost Episode\n\tBlanche - GOATed\n\tBlessed - Holy Music\n\tBoldAndBrash - "More like..."')
        
        await ctx.author.send('\tBomb - Return to sender\n\tBombPies - Knits you a sweater of tears, and you kill him\n\tBrothers - "Except closer"\n\tBullyMaguire - You\'re trash, Brock\n\tChanel - Not the cat\n\tCheer - Congrats\n\tChumIsFum - Plankton\'s what?\n\tCollege - Plankton\n\tCosmic - "You think this is funny?"\n\tCrackKid - "YAAAAAA"\n\tCrazyFrog - What\'s going on?\n\tCrickets - ...\n\tCurbYourEnthusiasm - Theme\n\tDaddy - Chill\n\tDefault - Jonesy Jams\n\tDietDrKelp - Krusty Krab Pizza [NO DRINK PRANK][GONE WRONG]\n\tEels - Tough luck\n\tElevatorMusic - Going up\n\tEMinor - Yeah! E Minor, alright!\n\tEnigma - *spills milk*\n\tFBI - Open up\n\tFirmlyGrasp - Squidward goes Jellyfishing\n\tFood - Don\'t forget the pickles\n\tFootLettuce - #12\n\tFuckYaLife - Bing Bong\n\tFunBegins - This is where\n\tGallon - Wacha got there?\n\tGaryNeedsShoes - DiceK-69\n\tGems - Outrageous\n\tHamlet - The vampires have invaded the castle\n\tHello - A bold one\n\tHesHot - Squidward Sus\n\tHeySquidward - Drink up\n\tHighGround - Surely this works\n\tHighTide - Thanks bubble buddy\n\tHolup - Wait a minute...\n\tHolyMoly - Old Man\n\tHoopla - Sounds like a lot of...\n\tICanExplain - Sandy commits house theft\n\tIncomplete - Perhaps...\n\tInevitable - Uh oh I hope no one takes the stones and kills themselves\n\tItsAllOver - Get up cocksuckers\n\tJohnCena - And his name is...\n\tKKPizza - For you and me\n\tLeak - Doodlebob strikes')
        
        await ctx.author.send('\tLeedleLeedleLee - Ghostly screech\n\tLiar - Pants on fire\n\tListeningTo - Commence gibberish\n\tLittleOne - Is he though?\n\tLobsters - Scorpions are cooler than lobsters, right?\n\tMagicConch - Maybe...\n\tMan - Spongebob shaves?\n\tMayonnaise - Musically gifted\n\tMilk - You can\'t\n\tMiScusi - Oui\n\tNavy - Robots have taken over\n\tNice - 69\n\tNoCaution - The Spins\n\tNoMoney - When you don\'t get the purple from CoX\n\tNonsense - Don\'t worry, we have technology\n\tNootNoot - Pingu\n\tNotFine - Tragic\n\tNuke - 25 Kill streak\n\tOhBrother - Stinky\n\tOldMan - I love the young people\n\tOof - Steve, no!\n\tOut - Goblin Mode Activated\n\tOvertime - You forgot your briefcase\n\tOwenWow - Classic\n\tPeerReviewed - Thanks Duke\n\tPinhead - I\'m Dirty Dan\n\tPizzaTime - He\'s late\n\tPodracing - Literally not but okay Anakin\n\tPotatoSalad - 3 Days\n\tPrepared - Not\n\tPrettyGood - Heyyy!\n\tProblem - \n\tR2 - Woooooo\n\tRemy - Speak!\n\tRick - Not his name\n\tRightBack - Not lol\n\tRisitas - E tu\n\tRock - Insert Dwayne Johnson\n\tRoommates - "Roommates"\n\tRunTheCord - How it feels\n\tSacrifice - Just business\n\tSadAirHorn - Misery\n\tSalad - What kind of salad is it?')
        
        await ctx.author.send('\tSand - Who wrote this movie\n\tScatman - RIP Legend\n\tScatmansWorld1 - Welcome to Scatman\'s world\n\tScatmansWorld2 - Hit it DJ\n\tSecondTime - Even funnier\n\tSheesh - Not iitzTimmy\n\tShrimp - Is that a...?\n\tSleeping - You fat fuck\n\tSmitty - It was his hat Mr. Krabs\n\tSnore - OOOOOOO\n\tSoiled - The good Krusty Krab name\n\tSparrow - The best he\'s ever seen\n\tSquidwardSmells - Good\n\tStarve - They stole a balloon\n\tSterile - Don\'t touch him\n\tStupidTown - Did you just blow in?\n\tSummer - 104 Days of Summer Vacation\n\tSun - Otto does an evil\n\tSurge - Kaboom\n\tSus - Amogus\n\tSweaterOfTears - Is this one better Squidward?\n\tTexas - What\'s the difference?\n\tTheLot - We\'ll take it!\n\tTheLot2 - U wot m8?\n\tThis - But Spongebob she NEEDS this\n\tThot - Begone\n\tTired - Grandpa I\'m tired\n\tTooDamnBad - Well that\'s too damn bad!\n\tTriple - MOM GET THE CAMERA\n\tUgly - Well...\n\tVictoryScreech - Ululating commences\n\tWaiting - *twiddles thumbs*\n\tWe#1 - Robbie Rotten\n\tWeast - What kind of compass are you reading?\n\tWeCanMakeIt - I can spit across that gap\n\tWednesday - My dudes\n\tWeLikeFortnite - Take the L\n\tWhatIsEven - WHAT THE HELL\n\tWhoAreYouPeople - Janet? Marty?\n\tWii - Best game system since 2008\n\tWomboCombo - That ain\'t Falco\n\tWumbo - Wumbology\n\tXfiles - It\'s out there\n\tYeahBaby - Thats what i\'ve been waiting for!\n\tYoshi - AAAAAAA\n\tYoureGood - We\'ll buff out those scratches\n\tYouWhat - !!!???\n\tZombie - YAAAAA')

    
    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""
        
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        
        await channel.connect()

    async def timeout():
        print('timeout started')
        try:
            await asyncio.sleep(300)
        except asyncio.CancelledError:
            print('cancel_me(): cancel sleep')
            raise
        finally:
            print('cancel_me(): after sleep')
        
            
    @commands.hybrid_command()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def play(self, ctx, *, query):
        """Plays a file from the local filesystem"""
        
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(SESource(query)), .25)
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
        task = asyncio.create_task(timeout())
        
        await asyncio.sleep(1)
        
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            print('main(): timeout is cancelled now')
        
        

        #await ctx.send('Now playing: {}'.format(query))
            

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
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
    '''
    await bot.get_channel(TestServer).send('To interact with this bot just mention me with the "@" symbol or use "~" with one of the following commands:\n\n~join - Joins a voice channel\n~volume x - Sets the volume to the integer x\n~stop - Stops and disconnects the bot from voice\n---------------------------------------------\n~play <name> - Plays the file <name> from the library below:\n\t#1 - Am I really going to deface this grave for money?\n\t3am - "Oh Boy! 3am!"\n\t4 - "Don\'t you have to be stupid somewhere else?"\n\tAdvancedDarkness - Rock Bottom\n\tAirhorn - Start your mixtape\n\tAllDay - America\'s Ass\n\tAwake - Todd Howard you son of a bitch\n\tBanjo - TWANG\n\tBarnacles - "This is a load of..."\n\tBarrage - PK\'d\n\tBathtub - No lifeguard on duty\n\tBeautiful - That hat makes you look...\n\tBeeBooBooBop - Nah man, you\'re thinking of...\n\tBelieve - Mr. Anderson\n\tBetaSonic - Thanks, Shadow.\n\tBetrayal - The Lost Episode\n\tBlanche - GOATed\n\tBlessed - Holy Music\n\tBoldAndBrash - "More like..."')
    await bot.get_channel(TestServer).send('\tBomb - Return to sender\n\tBombPies - Knits you a sweater of tears, and you kill him\n\tBrothers - "Except closer"\n\tBullyMaguire - You\'re trash, Brock\n\tChanel - Not the cat\n\tCheer - Congrats\n\tChumIsFum - Plankton\'s what?\n\tCollege - Plankton\n\tCosmic - "You think this is funny?"\n\tCrackKid - "YAAAAAA"\n\tCrazyFrog - What\'s going on?\n\tCrickets - ...\n\tCurbYourEnthusiasm - Theme\n\tDaddy - Chill\n\tDefault - Jonesy Jams\n\tDietDrKelp - Krusty Krab Pizza [NO DRINK PRANK][GONE WRONG]\n\tEels - Tough luck\n\tElevatorMusic - Going up\n\tEMinor - Yeah! E Minor, alright!\n\tEnigma - *spills milk*\n\tFBI - Open up\n\tFirmlyGrasp - Squidward goes Jellyfishing\n\tFood - Don\'t forget the pickles\n\tFootLettuce - #12\n\tFuckYaLife - Bing Bong\n\tFunBegins - This is where\n\tGallon - Wacha got there?\n\tGaryNeedsShoes - DiceK-69\n\tGems - Outrageous\n\tHamlet - The vampires have invaded the castle\n\tHello - A bold one\n\tHesHot - Squidward Sus\n\tHeySquidward - Drink up\n\tHighGround - Surely this works\n\tHighTide - Thanks bubble buddy\n\tHolup - Wait a minute...\n\tHolyMoly - Old Man\n\tHoopla - Sounds like a lot of...\n\tICanExplain - Sandy commits house theft\n\tIncomplete - Perhaps...\n\tInevitable - Uh oh I hope no one takes the stones and kills themselves\n\tItsAllOver - Get up cocksuckers\n\tJohnCena - And his name is...\n\tKKPizza - For you and me\n\tLeak - Doodlebob strikes')
    await bot.get_channel(TestServer).send('\tLeedleLeedleLee - Ghostly screech\n\tLiar - Pants on fire\n\tListeningTo - Commence gibberish\n\tLittleOne - Is he though?\n\tLobsters - Scorpions are cooler than lobsters, right?\n\tMagicConch - Maybe...\n\tMan - Spongebob shaves?\n\tMayonnaise - Musically gifted\n\tMilk - You can\'t\n\tMiScusi - Oui\n\tNavy - Robots have taken over\n\tNice - 69\n\tNoCaution - The Spins\n\tNoMoney - When you don\'t get the purple from CoX\n\tNonsense - Don\'t worry, we have technology\n\tNootNoot - Pingu\n\tNotFine - Tragic\n\tNuke - 25 Kill streak\n\tOhBrother - Stinky\n\tOldMan - I love the young people\n\tOof - Steve, no!\n\tOut - Goblin Mode Activated\n\tOvertime - You forgot your briefcase\n\tOwenWow - Classic\n\tPeerReviewed - Thanks Duke\n\tPinhead - I\'m Dirty Dan\n\tPizzaTime - He\'s late\n\tPodracing - Literally not but okay Anakin\n\tPotatoSalad - 3 Days\n\tPrepared - Not\n\tPrettyGood - Heyyy!\n\tProblem - \n\tR2 - Woooooo\n\tRemy - Speak!\n\tRick - Not his name\n\tRightBack - Not lol\n\tRisitas - E tu\n\tRock - Insert Dwayne Johnson\n\tRoommates - "Roommates"\n\tRunTheCord - How it feels\n\tSacrifice - Just business\n\tSadAirHorn - Misery\n\tSalad - What kind of salad is it?')
    await bot.get_channel(TestServer).send('\tSand - Who wrote this movie\n\tScatman - RIP Legend\n\tScatmansWorld1 - Welcome to Scatman\'s world\n\tScatmansWorld2 - Hit it DJ\n\tSecondTime - Even funnier\n\tSheesh - Not iitzTimmy\n\tShrimp - Is that a...?\n\tSleeping - You fat fuck\n\tSmitty - It was his hat Mr. Krabs\n\tSnore - OOOOOOO\n\tSoiled - The good Krusty Krab name\n\tSparrow - The best he\'s ever seen\n\tSquidwardSmells - Good\n\tStarve - They stole a balloon\n\tSterile - Don\'t touch him\n\tStupidTown - Did you just blow in?\n\tSummer - 104 Days of Summer Vacation\n\tSun - Otto does an evil\n\tSurge - Kaboom\n\tSus - Amogus\n\tSweaterOfTears - Is this one better Squidward?\n\tTexas - What\'s the difference?\n\tTheLot - We\'ll take it!\n\tTheLot2 - U wot m8?\n\tThis - But Spongebob she NEEDS this\n\tThot - Begone\n\tTired - Grandpa I\'m tired\n\tTooDamnBad - Well that\'s too damn bad!\n\tTriple - MOM GET THE CAMERA\n\tUgly - Well...\n\tVictoryScreech - Ululating commences\n\tWaiting - *twiddles thumbs*\n\tWe#1 - Robbie Rotten\n\tWeast - What kind of compass are you reading?\n\tWeCanMakeIt - I can spit across that gap\n\tWednesday - My dudes\n\tWeLikeFortnite - Take the L\n\tWhatIsEven - WHAT THE HELL\n\tWhoAreYouPeople - Janet? Marty?\n\tWii - Best game system since 2008\n\tWomboCombo - That ain\'t Falco\n\tWumbo - Wumbology\n\tXfiles - It\'s out there\n\tYeahBaby - Thats what i\'ve been waiting for!\n\tYoshi - AAAAAAA\n\tYoureGood - We\'ll buff out those scratches\n\tYouWhat - !!!???\n\tZombie - YAAAAA')
'''

bot.add_cog(Sound_Effect(bot))
    
MCantyBot_Token = 'OTg2MzI1NDY2NDMwNDM5NTM1.G2SDs-.W8w1ZcX-VCX2Z9fF_TmPOQlqk19A5hLgPjcQuU'
bot.run(MCantyBot_Token)
