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
