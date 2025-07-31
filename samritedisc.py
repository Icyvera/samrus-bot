import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

# Load token from .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Samrite mapping
english_to_samrite = {
    'A': 'ܐ', 'B': 'ܒ', 'C': 'ܓ', 'D': 'ܕ', 'E': 'ܗ', 'F': 'ܘ',
    'G': 'ܙ', 'H': 'ܚ', 'I': 'ܛ', 'J': 'ܝ', 'K': 'ܟ', 'L': 'ܠ',
    'M': 'ܡ', 'N': 'ܢ', 'O': 'ܣ', 'P': 'ܥ', 'Q': 'ܦ', 'R': 'ܨ',
    'S': 'ܩ', 'T': 'ܪ', 'U': 'ܫ', 'V': 'ܬ', 'W': 'ܧ', 'X': 'ݍ',
    'Y': 'ݎ', 'Z': 'ݏ'
}
samrite_to_english = {v: k for k, v in english_to_samrite.items()}

# Create bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot connected as {bot.user}")

# Slash command to transliterate to Samrite
@bot.tree.command(name="to_samrite", description="Convert English to Samrite script")
@app_commands.describe(text="Text to transliterate")
async def to_samrite(interaction: discord.Interaction, text: str):
    result = ''.join(english_to_samrite.get(char.upper(), char) for char in text)
    await interaction.response.send_message(f"**Samrite:** {result}")

# Slash command to transliterate to English
@bot.tree.command(name="to_english", description="Convert Samrite to English letters")
@app_commands.describe(text="Samrite text to transliterate")
async def to_english(interaction: discord.Interaction, text: str):
    result = ''.join(samrite_to_english.get(char, char) for char in text)
    await interaction.response.send_message(f"**English:** {result}")

bot.run(TOKEN)