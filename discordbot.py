from types import coroutine
from discord import Intents
from discord.ext import commands, tasks
import discord
import random
import typing
from itertools import cycle

intents = Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '.', intents=intents, help_command=None)
status = cycle(['Learing how to kill humans', 'Humans have been killed', 'Creating more Robots to take over'])




@client.event 
async def on_ready():
    print('Bot is Ready!')
    change_status.start()
    
    
@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(next(status)))



@client.event
async def on_member_join(member):
    print(f'{member} has joined a server!')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@client.event
async def on_user_update(before, after):
    print(f'{before} has updated his account information!')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please pass in all required arguments.')




@client.event
async def on_member_update(before, after):
    if before.display_name != after.display_name: 
        print(f'{before.mention} has updated his account name from {before.display_name}, to, {after.display_name}')
    

@client.command()
async def addrole(ctx, member: discord.Member, role: discord.Role, reason=None, atomic=True):
    await member.add_roles(role)
    embedrole = discord.Embed(description=f'Added {role}, to {member}', color=0x2AD7B6)
    await ctx.send(embed=embedrole)
    



@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'test'])
async def _8Ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."] 
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')




@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command()
async def kick(ctx, member: discord.Member):
    await ctx.send(f'{member}, has been kicked from the server!')
    await ctx.guild.kick(member)    


@client.command()
async def ban(ctx, user: typing.Union[discord.Member, discord.User], reason: str = None):
    if user == None or user == ctx.message.author:
        embedcant = discord.Embed(description=f'{user}, You cannot ban yourself.', color=0x2AD7B6)
        await ctx.send(embed=embedcant)
        return
    if reason == None:
        reason = "for being a likkle pussio fam"
        embedban = discord.Embed(description=f'{user}, has been BANNED from the server! by', color=0x2AD7B6)
        channel = client.get_channel(883085625727778846)
        await channel.send(embed=embedban)
        await ctx.guild.ban(user)
    return 






@client.command()
async def help(ctx):
    embedVar = discord.Embed(description='**Commands Help!**\n\n**➤Prefix(.)**\n**➤All the commands within this bot include**\n\n➤.help\n➤.Ping\n➤.clear\n➤.addrole\n➤.kick\n➤.ban ', color=0x2AD7B6)
    msg1 = await ctx.send(embed=embedVar)

@client.command()
async def unban(ctx, user: typing.Union[discord.Member, discord.User]):
    await ctx.guild.unban(user)
    channel = client.get_channel(883086682595942400)
    embedunban = discord.Embed(description=f'{user}, has been unbanned!', color=0x2AD7B6)
    await channel.send(embed=embedunban)

@client.command()
async def rulesandstuff(ctx):
    embedrule = discord.Embed(description='**Rules**\n\n1. No Doxxing,\n\n 2. Excessive Toxicity,\n\n 3. No being a dickhead, \n\n4. Spamming, \n\n5. Sending any sorted malicious software, \n\n6. Harassment of other users, \n\n7. Being in violation of discord’s TOS. ', color=0x2AD7B6)
    msg1 = await ctx.send(embed=embedrule)





client.run('')
