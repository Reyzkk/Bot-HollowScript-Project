import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

# Carrega o token do .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

class NexaBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()
        print("✅ Slash commands sincronizados.")

bot = NexaBot()

@bot.event
async def on_ready():
    print(f"🤖 Nexa está online como {bot.user}")

@bot.tree.command(name="ping", description="Responde com pong")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong!")

if TOKEN is None:
    print("❌ ERRO: Token não encontrado. Configure o .env")
else:
    bot.run(TOKEN)
