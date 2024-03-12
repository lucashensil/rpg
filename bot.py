import discord
import asyncio
from discord.ext import commands
from main import Visualizacao
from credencias import token

ultima_raca_solicitada = None  # Variável para armazenar o nome da última raça solicitada

class MyClient(discord.Client, Visualizacao):
    async def on_ready(self):
        self.visu = Visualizacao()
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith(f'!Raca'):
            global ultima_raca_solicitada
            nome = message.content.split(' ', 1)[1]
            resposta1 = self.visu.visuzalizar_raca(nome)
            await message.channel.send(resposta1)
            ultima_raca_solicitada = nome  

        if message.content.startswith(f'!Habilidades'):
            if ultima_raca_solicitada:  
                resposta2 = self.visu.visualizar_habs_raca(ultima_raca_solicitada)
                await message.channel.send(resposta2)
                ultima_raca_solicitada = None  
            else:
                await message.channel.send("Você não solicitou informações sobre nenhuma raça ainda.")


        if message.content.startswith(f'!Atributo'):
            atr = message.content.split(' ', 1)[1]
            resposta = self.visu.buscar_atributo(atr)
            await message.channel.send(resposta)

        if message.content.startswith(f'!Procurar Habilidade'):
            hab = message.content.split(' ', 1)[1]
            resposta = self.visu.buscar_habilidade(hab)
            await message.channel.send(resposta)

        if message.content.startswith(f'!Classe'):
            classe = message.content.split(' ', 1)[1]
            resposta = self.visu.visualiar_classe(classe)
            await message.channel.send(resposta)



intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token=token)
