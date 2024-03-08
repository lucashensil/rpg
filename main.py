import sqlite3


class Visualizacao():
    def __init__(self):
        self.conn = sqlite3.connect('rpg.db')

        self.cursor = self.conn.cursor()


    def visuzalizar_raca(self, raca_nome):

        raca = raca_nome.capitalize()

        self.cursor.execute(f'''SELECT 
                            nome_raca, 
                            descricao, 
                            idade, 
                            velocidade, 
                            alinhamento, 
                            medidas, 
                            hab_raciais,
                            atributo,
                            modificador
                            FROM racas 
                            INNER JOIN atributos_raciais 
                            ON racas.id_raca = atributos_raciais.id_raca WHERE nome_raca = "{raca}"''')

        info = self.cursor.fetchall()

        desc = info[0][1]
        idade = info[0][2]
        vel = info[0][3]
        alinhamento = info[0][4]
        med = info[0][5]
        hab = info[0][6]
        atr1 = info[0][7]
        mod1 = info[0][8]
        atr2 = info[1][7]
        mod2 = info[1][8]

        t = f'''
Raça: {raca}
{atr1} +{mod1}, {atr2} +{mod2}

Descrição: {desc}

Idade: {idade}

Velocidade: {vel}

Alinhamento: {alinhamento}

Tamanho: {med}

Habilidades Raciais: {hab}
        '''

        return t





