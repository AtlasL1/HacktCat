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
