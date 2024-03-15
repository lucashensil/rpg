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
            raca = self.visu.visuzalizar_raca(raca)
            await message.channel.send(raca)
            ultima_raca_solicitada = nome  

        if message.content.startswith(f'!Habilidades'):
            if ultima_raca_solicitada:  
                habilidades = self.visu.visualizar_habs_raca(ultima_raca_solicitada)
                await message.channel.send(habilidades)
                ultima_raca_solicitada = None  
            else:
                await message.channel.send("Você não solicitou informações sobre nenhuma raça ainda.")


        if message.content.startswith(f'!Atributo'):
            atr = message.content.split(' ', 1)[1]
            resposta = self.visu.buscar_atributo(atr)
            await message.channel.send(resposta)

        if message.content.startswith(f'!Procurar Habilidade'):
            hab = message.content[len('!Procurar Habilidade '):]
            racas = self.visu.buscar_habilidade(hab)
            subracas = self.visu.buscar_habilidade_subraca(hab)
            if racas:
                await message.channel.send(racas)
            else:
                await message.channel.send('Habilidade não encontrada em nenhuma raça')
            if subracas:
                await message.channel.send(subracas)
            elif not racas and not subracas:
                await message.channel.send('Habilidade não encontrada em nenhuma sub-raça')

        if message.content.startswith(f'!Classe'):
            nome = message.content.split(' ', 1)[1]
            classe = self.visu.visualizar_classe(nome)
            await message.channel.send(classe)



intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token=token)
