import discord
from discord.ext import commands
import google.generativeai as genai

generation_config = {
    "temperature": 0,
    "top_p": 1,
    "top_k": 1,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

model = genai.GenerativeModel(model_name='gemini-pro', generation_config=generation_config, safety_settings=safety_settings)
genai.configure(api_key='KEY')
bot = commands.Bot(command_prefix='!aix ', intents=discord.Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.custom, name=' ', state='Talk to me.'))
    await bot.tree.sync()
    print('Logged in as Hack the Cat [AI]#6452.')

def interact_with_black_cat(prompt):
    response = model.generate_content(prompt)
    return response.text

async def start_chat(message):
    response = interact_with_black_cat(f'{message.content}\nRespond in just one sentence and read the message content closely. Do not include any extra information to my message. You are a little snarky. You do like talking to people, however. You use casual English. You don\'t mention that you are passive-aggressive. You\'re just bored of life. If someone asks for your name, you tell them you are Black Cat. You are also a cat working under Cyberclaw & Co. and a game character created by Atlas. You are cold and passive aggressive most of the time, but enjoys the company of the traveller, who is the user talking to you, along with your best friend, ADHD Cat, who you call A. You have black fur and bright green eyes. You are a major technology enthusiast and talks in perfect but casual English. Don\'t add any other sentence that is not significant to my message.')
    if response.startswith('"'):
        response = response[1:]
        if response.endswith('"'):
            response = response[:-1]
    await message.reply(response)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if bot.user.mentioned_in(message):
        async with message.channel.typing():
            try:
                await start_chat(message)
            except Exception as e:
                embed = (
                    discord.Embed(
                        title='Error Logs',
                        description=f'An error has occured while processing your message:\n'
                                    f'```ansi\n\u001b[0;1;37m\u001b[0;1;37m{e}```',
                        colour=discord.Colour.red()
                    )
                )
                await message.channel.send(embed=embed)

    elif any(word in message.content.lower() for word in ["black cat", "htc", "hack"]):
        async with message.channel.typing():
            try:
                await start_chat(message)
            except Exception as e:
                embed = (
                    discord.Embed(
                        title='Error Logs',
                        description=f'An error has occured while processing your message:\n'
                                    f'```ansi\n\u001b[0;1;37m\u001b[0;1;37m{e}```'
                    )
                )
                await message.channel.send(embed=embed)

    await bot.process_commands(message)

bot.run('TOKEN')
