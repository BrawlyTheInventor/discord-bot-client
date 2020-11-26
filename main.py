import discord

TOKEN = input("Enter your Discord bot token")
channelvar = input("Enter channel")
print("Showing last messages")
class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
while True: 
    messages = await channelvar.history(limit=2).flatten()
    print(messages)
    await message.channel.send(input("Enter message to send")
        
client = CustomClient()
client.run(TOKEN)
