import discord
import responses


# function for default responses
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# function for running the bot
def run_discord_bot():
    TOKEN = 'MTE4Mzk4NjM4OTUwNzkwMzU0OQ.G6f0xw.PT8uiXbze0sNblO14aV_DqE4UkQuLRUxEa7--8' #it has already been changed, do not worry
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # prints when bot is running
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    # response triggered by message sent event
    @client.event
    # prevents bot from looping and replying to itself
    async def on_message(message):
        if message.author == client.user:
            return
        # initializes variable for following loops and if statements
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        botname = str('<@1183986389507903549>')  # bot id number in discord
        theo = str('<@562143920746659841>')     # specific id number of a user in discord
        # prints username, message, and channel in console when message sent in discord
        print(f'{username} said: "{user_message}" ({channel})')
        # specific response to anything a specific user says
        if username == 'thermuss':
            response = "shut yo ass up thompo"
            await message.channel.send(response)
        # specific response when bot is pinged in a server
        for x in range(len(user_message) + 1 - len(botname)):
            if user_message[x:x + len(botname)] == botname:
                response = "don't ping me mf"
                await message.channel.send(response)

        # specific response for when a specific user is pinged in a server
        for x in range(len(user_message) + 1 - len(theo)):
            if user_message[x:x + len(theo)] == theo:
                response = "do we really need to listen to what he has to say"
                await message.channel.send(response)
        # enables recognition of a command
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
