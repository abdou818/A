from discord.ext import commands
import discord

TOKEN = "MTMzNjg3MDA4MzM1MTQxNjgzMg.GVuTZ0.ASc-h7VAatch6oRUIpwGWJcrqPyssT_yb35b7Y"
GUILD_ID = 1387106900390449203
VOICE_CHANNEL_ID = 1387106900390449203

bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    guild = bot.get_guild(GUILD_ID)
    channel = guild.get_channel(VOICE_CHANNEL_ID)
    await channel.connect()
    print("✅ دخل الروم الصوتي")

bot.run(TOKEN)
