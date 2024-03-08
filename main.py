import sqlite3


class Visualizacao():
    def __init__(self):
        self.conn = sqlite3.connect('rpg.db')

        self.cursor = self.conn.cursor()


    def visuzalizar_raca(self, raca_nome):

        raca = raca_nome.capitalize()

        self.cursor.execute(f"SELECT nome_raca, descricao, idade, velocidade, alinhamento, medidas, hab_raciais FROM racas WHERE nome_raca = '{raca}'")

        info = self.cursor.fetchall()[0]

        desc = info[1]
        idade = info[2]
        vel = info[3]
        alinhamento = info[4]
        med = info[5]
        hab = info[6]

        t = f'''
Raça: {raca}

Descrição: {desc}

Velocidade: {vel}

Alinhamento: {alinhamento}

Tamanho: {med}

Habilidades Raciais: {hab}
        '''

        return t
