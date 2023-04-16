from discord.ext import commands
import discord

try:
    import uvloop
except ImportError:
    pass
else:
    uvloop.install()
import os


bot = commands.Bot(command_prefix="demo!", intents=discord.Intents.all())


if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_TOKEN"))
