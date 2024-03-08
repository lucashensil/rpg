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


cursor.execute('SELECT id_raca FROM atributos_raciais WHERE atributo = "Destreza" ')
ids = cursor.fetchall()
consultas = []
for id_ in ids:
    id_raca = id_[0]

    cursor.execute(f'''SELECT 
                        nome_raca, 
                        atributo,
                        modificador
                        FROM racas 
                        INNER JOIN atributos_raciais 
                        ON racas.id_raca = atributos_raciais.id_raca 
                        WHERE atributos_raciais.id_raca = "{id_raca}" ''')
    
    resultado = cursor.fetchall()
    consultas.append(resultado)
    


for consulta in consultas:
    if len(consulta) == 2:
        item1, item2 = consulta
        raca, atr1, valor1 = item1
        raca, atr2, valor2 = item2

        print(f'''Raca: {raca}, {atr1}: +{valor1}; {atr2}: +{valor2}''')
    
    if len(consulta) == 1:
        raca, atr1, valor1 = consulta[0]
        print(f'''Raca: {raca}, {atr1}: +{valor1};''')


