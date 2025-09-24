import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

class NexaBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)
        # NÃO precisa criar o CommandTree aqui!

    async def setup_hook(self):
        await self.tree.sync()  # sincroniza os comandos globalmente

bot = NexaBot()

@bot.event
async def on_ready():
    print(f"HollowScript está online como {bot.user}")

@bot.tree.command(name="ping", description="Responde com pong")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong!")

bot.run(TOKEN)
