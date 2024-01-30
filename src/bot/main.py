# Hack the Cat
# Discord Bot

import discord
from discord.ext import commands
from discord.ui import Select, View
import asyncio
import sqlite3

TOKEN = 'TOKEN'
bot = commands.Bot(command_prefix='!x ', intents=discord.Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.custom, name=' ', state='Chapter 1: Coming Soon.'))
    await bot.tree.sync()
    print('Logged in as Hack the Cat!#0092.')

class HelpSelect(Select):
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == 'game':
            embed = (
                discord.Embed(
                    title='Hack the Cat',
                    description='Using Hack the Cat is very simple.\n\n'
                                'To start the game, you use: `!x start`. \nThis command is the English version of the game, which is the default.\n\n'
                                'You do not have to worry about the rest. You will be taught along the way. Have fun!\n\n',
                    colour=discord.Colour.from_rgb(1, 1, 1)
                )
            )
            embed.set_image(
                url='https://i.pinimg.com/564x/cd/9c/ac/cd9cace9ae1f869c21bcd1da78c3a22f.jpg'
            )
            await interaction.response.send_message(embed=embed)
        elif self.values[0] == 'general':
            embed = (
                discord.Embed(
                    title='Hack the Cat (HTC) General Commands',
                    colour=discord.Colour.from_rgb(1, 1, 1)
                )
            )
            embed.set_thumbnail(
                url=bot.user.avatar.url
            )
            embed.add_field(
                name='Info',
                value='- </bot-info:1156878340607709184>\n',
                inline=False
            )
            embed.add_field(
                name='New',
                value='- </htc-updates:1156885460287754260>\n'
                      '- </htc-changelog:1156885460287754261>\n',
                inline=False
            )
            embed.add_field(
                name='Uncategorised',
                value='- </htc-comment:1156885952279629904>\n'
                      '- </htc-partners:1156878340607709186>\n'
                      '- </cat-gen:1156878340607709185>\n'
                      '- </invite-htc:1156885460287754262>',
                inline=False
            )
            await interaction.response.send_message(embed=embed)

class HelpOptions(View):
    def __init__(self):
        super().__init__()
        self.add_item(HelpSelect(
            options=[
                discord.SelectOption(
                    label='Game Commands',
                    description='Game commands of HTC',
                    emoji='<:blackcatgame:1194178066407227392>',
                    value='game'
                ),
                discord.SelectOption(
                    label='General Commands',
                    description='General commands of HTC',
                    emoji='<:blackcatgeneral:1194178125559500812>',
                    value='general'
                )
            ]
        ))


@bot.command(name='help')
async def help(ctx):
    atlas = bot.get_user(860794014764105729)
    embed = (
        discord.Embed(
            title='Notice',
            description='This bot is reserved for the official Hack the Cat and is currently privately managed.\n',
            colour=discord.Colour.from_rgb(1, 1, 1)
        )
    )
    embed.set_image(
        url='https://i.pinimg.com/564x/89/9f/3d/899f3d319b77a8183c71fe5a57a5e689.jpg'
    )
    embed.set_author(
        icon_url=atlas.avatar.url,
        name='Atlas'
    )
    await ctx.send(embed=embed, view=HelpOptions())

@bot.tree.command(name='help', description='Learn how to use Hack the Cat.')
async def help(interaction):
    atlas = bot.get_user(860794014764105729)
    embed = (
        discord.Embed(
            title='Notice',
            description='This bot is reserved for the official Hack the Cat and is currently privately managed.\n',
            colour=discord.Colour.from_rgb(1, 1, 1)
        )
    )
    embed.set_image(
        url='https://i.pinimg.com/564x/89/9f/3d/899f3d319b77a8183c71fe5a57a5e689.jpg'
    )
    embed.set_author(
        icon_url=atlas.avatar.url,
        name='Atlas'
    )
    await interaction.response.send_message(embed=embed, view=HelpOptions())

class ChapterView(discord.ui.View):
    @discord.ui.button(label='Chapter 1', style=discord.ButtonStyle.grey, row=0)
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.button_callback.disabled = True
        await interaction.response.edit_message(view=self)
        embed = (
            discord.Embed(
                title='Chapter 1',
                description='You have chosen Chapter 1. \n'
                            'Please click on the following button to start. \n'
                            'If you wish to skip to another chapter, you may ignore this and rerun `!x start`.',
                colour=discord.Colour.from_rgb(1, 1, 1)
            )
        )
        class Chapter1Start(discord.ui.View):
            @discord.ui.button(label='Start', style=discord.ButtonStyle.grey, row=0)
            async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
                self.button_callback.disabled = True
                await interaction.response.edit_message(view=self)
                await interaction.followup.send('Welcome to our world.')
                await asyncio.sleep(1)
                await interaction.channel.send('I will be your narrator for this chapter.')
                await asyncio.sleep(1)
                await interaction.channel.send('Before you join, you\'ll need to read and accept the [terms of service](https://htc.is-local.org/tos.html) and [privacy policy](https://htc.is-local.org/pri.html).')
                await asyncio.sleep(1)
                await interaction.channel.send('If you already have, you may ignore it and click on the button.')
                await asyncio.sleep(1)

                class ToSSelect(Select):
                    async def callback(self, interaction: discord.Interaction):
                        if self.values[0] == 'tos':
                            tos_embed = (
                                discord.Embed(
                                    title='Terms of Service',
                                    description='**Warning: Violating the Terms of Service may result in being blacklisted or further actions.**',
                                    colour=discord.Colour.from_rgb(1, 1, 1)
                                )
                            )
                            tos_embed.add_field(
                                name='Usage of Hack the Cat',
                                value='1.1.1 Upon usage of Hack the Cat#1409, you acknowledge and agree that the bot is not completely free from errors.\n'
                                      '1.1.2 Your permission to use Hack the Cat is only granted upon using it for its intended purposes and in compliance with Discord\'s ToS.\n'
                                      '1.1.3 Hack the Cat cannot be used for any illegal actions or violate any laws and/or regulations.\n'
                                      '1.1.4 Using Hack the Cat to propagate any Not Safe For Work (NSFW) content is strictly prohibited and may result in permanent blacklisting.',
                                inline=False
                            )
                            tos_embed.add_field(
                                name='Data Collection & Privacy',
                                value='1.2.1 Hack the Cat collects a small amount of certain user data, e.g. user inputs. This is only for the purpose to provide its functionalities.\n'
                                      '1.2.2 Any user data collected by Hack the Cat will remain strictly confidential unless sharing is required by law.\n'
                                      '1.2.3 However, by using Hack the Cat, you acknowledge and accept the risks of data transmission over the Internet world. While data collection is protected, absolute security cannot be guaranteed.\n'
                                      '1.2.4 You acknowledge and agree that using any illegal tactics to access Hack the Cat\'s data collection is strictly prohibited.',
                                inline=False
                            )
                            await interaction.response.edit_message(embed=tos_embed)
                        elif self.values[0] == 'pri':
                            pri_embed = (
                                discord.Embed(
                                    title='Privacy Policy',
                                    description='2.1 Hack the Cat may store the following data: User input, user avatar and user display name. The data is usually stored for a very limited time and will automatically be deleted.\n'
                                                '2.2 The collection of user IDs is only during the condition when the Supreme Version of Hack the Cat is redeemed.\n'
                                                '2.3 Any data collected by Hack the Cat will not be shared or sold to any third parties unless it is required by law.\n'
                                                '2.4 Although Hack the Cat is suitable for users of all ages, Discord\'s Terms of Service must still be followed. Unless under the guidance of a user over the age of 13, no children is allowed to use Hack the Cat through an account that is against Discord\'s law.',
                                    colour=discord.Colour.from_rgb(1, 1, 1)
                                )
                            )
                            await interaction.response.edit_message(embed=pri_embed)

                class ToSOptions(discord.ui.View):
                    def __init__(self):
                        super().__init__()
                        self.add_item(ToSSelect(
                            options=[
                                discord.SelectOption(
                                    label='Terms of Service',
                                    description='Hack the Cat\'s terms of service.',
                                    emoji='<:tos:1200745936826138644>',
                                    value='tos'
                                ),
                                discord.SelectOption(
                                    label='Privacy Policy',
                                    description='Hack the Cat\'s privacy policy.',
                                    emoji='<:pri:1200745620382683186>',
                                    value='pri'
                                )
                            ],
                            row=0
                        ))

                    @discord.ui.button(emoji='<:black_tick:1195580148305641534>', label=' ', style=discord.ButtonStyle.grey, row=1)
                    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
                        self.button_callback.disabled = True
                        await interaction.response.edit_message(view=self)
                        tos_logging = bot.get_channel(1201025667442167828)
                        embed = (
                            discord.Embed(
                                title='Terms of Service & Privacy Policy Acceptance',
                                description='The following user has accepted the terms of service of Hack the Cat in the following guild:',
                                colour=discord.Colour.from_rgb(1, 1, 1)
                            )
                        )
                        embed.add_field(
                            name='USER INFO',
                            value=f'**Display Name**: {interaction.user.display_name}\n'
                                  f'**Username**: {interaction.user.name}\n'
                                  f'**ID**: {interaction.user.id}',
                            inline=False
                        )
                        embed.add_field(
                            name='GUILD INFO',
                            value=f'**Guild Name**: {interaction.guild.name}\n'
                                  f'**ID**: {interaction.guild.id}',
                            inline=False
                        )
                        embed.set_thumbnail(url=interaction.user.avatar)
                        embed.set_footer(text='ⓘ This information is strictly confidential and is only to maintain the safety and security of the bot\'s usage.')
                        await tos_logging.send(embed=embed)
                        await asyncio.sleep(1)
                        await interaction.channel.send('Very well.')
                        await asyncio.sleep(1)
                        await interaction.channel.send('I will now bring you to the waiting area.')
                        await asyncio.sleep(1)
                        await interaction.channel.send('')

                tos_embed = (
                    discord.Embed(
                        title='Terms of Service',
                        description='**Warning: Violating the Terms of Service may result in being blacklisted or further actions.**',
                        colour=discord.Colour.from_rgb(1, 1, 1)
                    )
                )
                tos_embed.add_field(
                    name='Usage of Hack the Cat',
                    value='1.1.1 Upon usage of Hack the Cat#1409, you acknowledge and agree that the bot is not completely free from errors.\n'
                          '1.1.2 Your permission to use Hack the Cat is only granted upon using it for its intended purposes and in compliance with Discord\'s ToS.\n'
                          '1.1.3 Hack the Cat cannot be used for any illegal actions or violate any laws and/or regulations.\n'
                          '1.1.4 Using Hack the Cat to propagate any Not Safe For Work (NSFW) content is strictly prohibited and may result in permanent blacklisting.',
                    inline=False
                )
                tos_embed.add_field(
                    name='Data Collection & Privacy',
                    value='1.2.1 Hack the Cat collects a small amount of certain user data, e.g. user inputs. This is only for the purpose to provide its functionalities.\n'
                          '1.2.2 Any user data collected by Hack the Cat will remain strictly confidential unless sharing is required by law.\n'
                          '1.2.3 However, by using Hack the Cat, you acknowledge and accept the risks of data transmission over the Internet world. While data collection is protected, absolute security cannot be guaranteed.\n'
                          '1.2.4 You acknowledge and agree that using any illegal tactics to access Hack the Cat\'s data collection is strictly prohibited.',
                    inline=False
                )
                await interaction.channel.send(embed=tos_embed, view=ToSOptions())

        await interaction.followup.send(embed=embed, view=Chapter1Start())

    @discord.ui.button(label='Chapter 2', style=discord.ButtonStyle.grey, row=0, disabled=True)
    async def button_callback2(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass

@bot.command(name='start')
async def start(ctx):
    embed = (
        discord.Embed(
            title='Enjoy.',
            description='Please select one of the chapters below.',
            colour=discord.Colour.from_rgb(1, 1, 1)
        )
    )
    embed.set_image(
        url='https://i.pinimg.com/564x/d4/3e/e2/d43ee204922d0939c1c1c4c3bfe947d0.jpg'
    )
    await ctx.send(embed=embed, view=ChapterView())

bot.run(TOKEN)
