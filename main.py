import discord, os
from discord.ext import commands
from deep_translator import GoogleTranslator
from language_codes import languages
from dotenv import load_dotenv

load_dotenv()
client = commands.Bot(command_prefix='-', intents=discord.Intents.all())
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('-help'))

@client.command(name='help')
async def help_command(message, arg=None):
    if arg is None:
        help_msg = {
            "title": "🖋️ Main Menu",
            "description": (
                "Type `-help command` for more info on a command.\n\n"
                "**Commands:**\n"
                "`-t lang text` - Translates your text to a specified language\n"
            )
        }
        await message.channel.send(embed=discord.Embed.from_dict(help_msg))


@client.command()
async def t(message, target: str, *, text: str):
    if target.lower() in languages or target.lower() in languages.values():
        translated = GoogleTranslator(source='auto', target=target).translate(text=text)
        await message.channel.send(translated)
    else:
        await message.channel.send("Invalid target language")


client.run(os.environ['LINGUABYTE_TOKEN'])
