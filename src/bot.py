import discord
from util import is_british

class SegFartBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents=intents)
    
    async def on_ready(self):
        print(f"Woahw!!! logged in as segfart yuh: {self.user}")

    async def on_message(self, message: discord.Message):
        # Punish the british
        if is_british(message.author):
            await message.add_reaction("🇬🇧")