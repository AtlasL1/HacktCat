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
