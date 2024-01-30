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
