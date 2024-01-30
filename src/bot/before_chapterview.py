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
