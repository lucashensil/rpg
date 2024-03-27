import discord
import asyncio
from discord.ext import commands
from main import Visualizacao
from credencias import token



class MyClient(discord.Client, Visualizacao):
    async def on_ready(self):
        self.visu = Visualizacao()
        self.ultima_raca_solicitada = None  # Variável para armazenar o nome da última raça solicitada
        self.ultima_subraca_solicitada = None  # Variável para armazenar o nome da última sub-raça solicitada

        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith(f'!Raca'): # Mostra todas as Racas
            
            nome = message.content.split(' ', 1)[1]
            raca = self.visu.visualizar_raca(nome)
            await message.channel.send(raca)
            self.ultima_raca_solicitada = nome  

        if message.content.startswith(f'!Subracas'): # Mostra todas as Sub-racas
            subraca = self.visu.buscar_subraca(self.ultima_raca_solicitada)
            await message.channel.send(subraca)

        if message.content.startswith(f'!Subraca'): # Mostra apenas uma sub-raca espeficia
            nome = message.content.split(' ', 1)[1]
            subraca = self.visu.visualizar_subraca(nome)
            await message.channel.send(subraca)
            self.ultima_subraca_solicitada = nome 

        if message.content.startswith(f'!Sub Habilidades'): # Habilidades sub-raca
            if self.ultima_subraca_solicitada:
                habilidades = self.visu.visualizar_habs_subraca(self.ultima_subraca_solicitada)
                await message.channel.send(habilidades)
                self.ultima_subraca_solicitada = None
            else:
                await message.channel.send("Você não solicitou informações sobre nenhuma sub-raça ainda.")

        if message.content.startswith(f'!Habilidades'): # Habilidades Raca
            if ultima_raca_solicitada:  
                habilidades = self.visu.visualizar_habs_raca(ultima_raca_solicitada)
                await message.channel.send(habilidades)
                ultima_raca_solicitada = None  
            else:
                await message.channel.send("Você não solicitou informações sobre nenhuma raça ainda.")


        if message.content.startswith(f'!Atributo'): # Busca racas com o atributo especifico
            atr = message.content.split(' ', 1)[1]
            resposta = self.visu.buscar_atributo(atr)
            await message.channel.send(resposta)

        if message.content.startswith(f'!Procurar Habilidade'): # Procura racas com a habilidade especifica
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

        if message.content.startswith(f'!Classe'): # Mostra as informacoes de uma classe
            nome = message.content.split(' ', 1)[1]
            classe = self.visu.visualizar_classe(nome)
            await message.channel.send(classe)

        if message.content.startswith(f'!Tabela'): # Mostra a tabela de evolucao de uma classe
            classe = message.content.split(' ', 1)[1]
            caminho = self.visu.visualizar_imagem_classe(classe)
            with open(caminho, 'rb') as file:
                picture = discord.File(file)
                

            await message.channel.send(file=picture)






intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token=token)
