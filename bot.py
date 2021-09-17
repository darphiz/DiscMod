import os
from dotenv import load_dotenv
from discord.ext import commands
from mod_api import check_nudity, check_profanity

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    contains_profanity = check_profanity(message.content)
    contains_nude = False
    guild = message.guild
    author = await guild.fetch_member(message.author.id)
    roles = [role.name for role in author.roles]
    if message.attachments:
        for file in message.attachments:
            is_nude = check_nudity(file.url)
            if is_nude:
                contains_nude = True
    text = f"Dear {message.author.name} \, you have been kicked from our community for violating our community standards, we wish you best of luck. The message that got you kicked => \"{message.content}\""
    
    if contains_profanity or contains_nude:
        if not "admin" in roles:
            try:
                await message.author.send(text)
            except:
                pass
            await message.channel.send(f"{message.author} has been kicked by {bot.user.name} for violating the community guildlines")
            message.author.kick()
        else:
            await message.author.send(f"Please watch your word ==> {message.content}")


bot.run(TOKEN)