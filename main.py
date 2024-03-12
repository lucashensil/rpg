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

        desc, idade, vel, alinhamento, med, hab, atr1, mod1 = info[0][1:9]

        if len(info) > 1:
            atr2, mod2 = info[1][7:9]
            mod1 = str(mod1) + ','
            mod2 = '+' + str(mod2)
        else:
            atr2 = ''
            mod2 = ''

        t = f'''
Raça: {raca}
{atr1} +{mod1} {atr2} {mod2}

Descrição: {desc}

Idade: {idade}

Velocidade: {vel}

Alinhamento: {alinhamento}

Tamanho: {med}

Habilidades Raciais: {hab}
        '''

        return t
    
    def buscar_atributo(self, atributo):

        self.cursor.execute(f'SELECT id_raca FROM atributos_raciais WHERE atributo = "{atributo}" ')
        ids = self.cursor.fetchall()
        consultas = []
        infos = []
        for id_ in ids:
            id_raca = id_[0]

            self.cursor.execute(f'''SELECT 
                                nome_raca, 
                                atributo,
                                modificador
                                FROM racas 
                                INNER JOIN atributos_raciais 
                                ON racas.id_raca = atributos_raciais.id_raca 
                                WHERE atributos_raciais.id_raca = "{id_raca}" ''')
            
            resultado = self.cursor.fetchall()
            consultas.append(resultado)
            


        for consulta in consultas:
            if len(consulta) == 2:
                item1, item2 = consulta
                raca, atr1, valor1 = item1
                raca, atr2, valor2 = item2
                
                t = f'''Raça: {raca}, {atr1}: +{valor1}; {atr2}: +{valor2}'''
                infos.append(t)
                
            
            if len(consulta) == 1:
                raca, atr1, valor1 = consulta[0]
                t = f'''Raça: {raca}, {atr1}: +{valor1};'''
                infos.append(t)


        info = '\n'.join(infos)
        return info

    def buscar_habilidade(self, hab_procurada):
            self.cursor.execute('SELECT nome_raca, hab_raciais FROM racas')


            infos = []
            consulta = self.cursor.fetchall()
            for habs in consulta:
                raca = habs[0]
                for hab in habs:
                    if hab_procurada in str(hab):
                        t = f''' Raça: {raca}, Habilidades: {hab} '''
                        infos.append(t)

            info = '\n'.join(infos)

            return(info)
    
    def visualizar_classe(self, classe):
        self.cursor.execute(f''' SELECT
                    id_classe, 
                    descricao, 
                    dados_vida, 
                    pontos_vida, 
                    pontos_vida_superior, 
                    proficiencias, 
                    equipamento
                    FROM classes
                    WHERE nome_classe = "{classe}"
                     ''')


        info = self.cursor.fetchall()[0]
        id_classe = info[0]
        descricao = info[1]
        dados_vida = info[2]
        pontos_vida = info[3]
        vida_superior = info[4]
        proficiencias = info[5]

        proficiencias = proficiencias.split(';')
        p_armadura = proficiencias[0]
        p_armas = proficiencias[1]
        p_ferramentas = proficiencias[2]
        p_resistencias = proficiencias[3]
        p_pericias = proficiencias[4]

        equipamento = info[6]


        t = f''' 
Classe: {classe}

Descrição: 
{descricao}

Dados de Vida: {dados_vida}
Pontos de Vida no 1º Nível: {pontos_vida}
Pontos de Vida em Níveis Superiores: {vida_superior}

Proficiências: 
 {p_armadura}
{p_armas}
{p_ferramentas}
{p_resistencias}
{p_pericias}

Equipamento Inicial:
{equipamento}
 '''
        
        return t
    
    def visualizar_habs_raca(self, raca):
        
        self.cursor.execute(''' SELECT id_raca, nome_raca FROM racas''')
        ids = self.cursor.fetchall()
        for id_ in ids:
            id_certo = id_[0]
            nome = id_[1]
            if nome == raca:
                self.cursor.execute(f''' SELECT nome_recurso, descricao
                                    FROM recursos_racas 
                                    WHERE id_raca = {id_certo} ''')
                info = self.cursor.fetchall()

        msgs = []

        for conteudo in info:
            hab = conteudo[0]
            desc = conteudo[1]
            
            msg = f'''{hab}: {desc}'''
            msgs.append(msg)

        t = '\n\n'.join(msgs)


        return t