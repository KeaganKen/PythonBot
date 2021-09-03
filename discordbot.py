from discord import Intents
from discord.ext import commands
import discord
import random
import typing


intents = Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '.', intents=intents, help_command=None)


@client.event 
async def on_ready():
    print('Bot is Ready!')
    

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
async def on_member_update(before, after):
    if before.display_name != after.display_name: 
        print(f'{before.mention} has updated his account name from {before.display_name}, to, {after.display_name}')
    


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
        
    








@client.command()
async def unban(ctx, user: discord.User):
    await ctx.guild.unban(user)
    print(f'{user} has been unbanned from the server')
    channel = client.get_channel(883086682595942400)
    embedunban = discord.Embed(description=f'{user}, has been unbanned from the server!', color=0x2AD7B6)
    msg1 = await channel.send(embed=embedunban)
    if user.ban == False:
        ctx.send("User is not banned")
    return






@client.command()
async def help(ctx):
    embedVar = discord.Embed(description='**Commands Help!**\n\n➤The prefix for this bot is a peroid (.)\n➤All the commands within this bot include\n➤.help\n➤.Ping which will show you the ping the bot is on\n ', color=0x2AD7B6)
    msg1 = await ctx.send(embed=embedVar)

@client.command()
async def is_banned(ctx, user_id : int, user: discord.user):
    user = client.get_user(user_id)
    try:
        await ctx.guild.fetch_ban(user)
    except discord.NotFound:
        await user.send('You are not in the ban list')
        return
    await ctx.send(f'{user.name} is in the ban list')

@client.command()
async def banned(ctx, response, message, user:discord.User):       
    try:
        await user.ban()
    except discord.HttpException(response, message):
        if response.status == 400:
            await ctx.send("This user is already banned")

client.run('ODgyNjUwOTM1OTE3MTU0Mzc0.YS-evQ.9PCnKq7NoRlAn4pZGLOQat6yRJk')