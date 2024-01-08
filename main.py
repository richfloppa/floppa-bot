import discord
from discord.ext import commands
from datetime import date
from keep_alive import keep_alive
keep_alive()


intents = discord.Intents.all()
intents.members = True

prefixes = ["r!", "R!", " <@1133486025025519748>"]

bot = commands.Bot(command_prefix=prefixes, intents=intents)
        
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name="discord.gg/rfserver"))

target_server_id = 752871508912767027 

@bot.event
async def on_member_join(member):
    christmas_emoji_enter = "<a:christimas_floppa_enter:1189523115160641616>"
    normal_emoji_enter = "<a:floppa_enter:1189523017240412220>"

    if is_christmas():
        emoji = christmas_emoji_enter
    else:
        emoji = normal_emoji_enter

    channel_id = 752887750000246795  # Replace with your channel ID
    channel = bot.get_channel(channel_id)

    if member.guild.id == target_server_id:
        member_count = len(member.guild.members)
        remaining_members = max(0, 1000 - member_count)

        if remaining_members == 0:
            await channel.send(f"{emoji} {member.mention} **has joined the server,** **We are now 1000 members!** @everyone")
        else:
            await channel.send(f"{emoji} {member.mention} **has joined the server** `{remaining_members}` **members remaining to reach** `1000` **member goal.**")

@bot.event
async def on_member_remove(member):
    christmas_emoji_exit = "<a:christimas_floppa_exit:1189523288829997068>"
    normal_emoji_exit = "<a:floppa_exit:1189523327103008848>"

    if is_christmas():
        emoji = christmas_emoji_exit
    else:
        emoji = normal_emoji_exit

    channel_id = 752887750000246795  # Replace with your channel ID
    channel = bot.get_channel(channel_id)

    if member.guild.id == target_server_id:
        member_count = len(member.guild.members)
        remaining_members = max(0, 1000 - member_count)
        await channel.send(f"{emoji} {member.mention} **has left the server**,`{remaining_members}` **members remaining to reach** `1000` **member goal**")

def is_christmas():
    today = date.today()
    return today.month == 12 and today.day == 25


import os

@bot.event
async def on_disconnect():
    print("Bot disconnected. Reconnecting...")

@bot.event
async def on_error(event, *args, **kwargs):
    print(f"Error in {event}: {args[0]}")
    if isinstance(args[0], discord.ConnectionClosed):
        print("Reconnecting...")
        await asyncio.sleep(5)  # Add a delay before attempting to reconnect
        await bot.login(token, bot=True)
        await bot.connect()

token = os.getenv("token")

if token is None:
    print("Error: Token not found in environment variables.")
else:
    bot.run(token)
