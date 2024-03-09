import discord
from main import Visualizacao
from credencias import token


class MyClient(discord.Client, Visualizacao):
    async def on_ready(self):
        self.visu = Visualizacao()
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith(f'!Raca'):
            nome = message.content.split(' ', 1)[1]
            resposta = self.visu.visuzalizar_raca(nome)
            await message.channel.send(resposta)

        if message.content.startswith(f'!Atributo'):
            atr = message.content.split(' ', 1)[1]
            resposta = self.visu.buscar_atributo(atr)
            await message.channel.send(resposta)

        if message.content.startswith(f'!Habilidade'):
            hab = message.content.split(' ', 1)[1]
            resposta = self.visu.buscar_habilidade(hab)
            await message.channel.send(resposta)



intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token=token)
