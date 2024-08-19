@bot.tree.command(name='blague', description="Raconte une blague")

async def blague_command(interaction: discord.Interaction,):

    try:

        # Attempt to get a random joke

        blague = await blagues.random()

        joke_message = f"Blague: {blague.joke}\nRéponse: ||{blague.answer}||"

        await interaction.response.send_message(joke_message)

    except Exception as e:

        await interaction.response.send_message(f"Erreur lors de la récupération de la blague : {str(e)}")  
    
blagues = BlaguesAPI("Token à récuper sur blagues-api.fr")
