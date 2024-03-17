import sqlite3


class Visualizacao():
    def __init__(self):
        self.conn = sqlite3.connect('rpg.db')

        self.cursor = self.conn.cursor()

    def visuzalizar_raca(self, raca_nome):
        """Visualiza as informações de uma raça específica.

        Args:
            raca_nome (str): O nome da raça a ser visualizada.

        Returns:
            str: Uma string formatada contendo as informações da raça.
        """
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
        subracas = self.buscar_subraca(raca_nome)

        if len(info) > 1:
            atr2, mod2 = info[1][7:9]
            mod1 = str(mod1) + ','
            mod2 = '+' + str(mod2)
        else:
            atr2 = ''
            mod2 = ''

        if subracas != '':
            subracas = f'Sub-Raças: {subracas}\n'
        t = f'''
Raça: {raca}
{atr1} +{mod1} {atr2} {mod2}
{subracas}
Descrição: {desc}

Idade: {idade}

Velocidade: {vel}

Alinhamento: {alinhamento}

Tamanho: {med}

Habilidades Raciais: {hab}
        '''

        return t
    
    def buscar_subraca(self, raca):
        self.cursor.execute(f'SELECT nome_subraca FROM subracas INNER JOIN racas on subracas.id_raca = racas.id_raca WHERE nome_raca = "{raca}"')

        subracas = self.cursor.fetchall()
        infos = []
        for sub in subracas:
            t = f'{sub[0]}'
            infos.append(t)

        info = ', '.join(infos)
        return info

    def buscar_atributo(self, atributo):
        """Busca as raças que possuem um atributo específico.

        Args:
            atributo (str): O atributo a ser buscado.

        Returns:
            str: Uma string contendo as raças e os atributos encontrados.
        """

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
        """Busca raças que possuem uma habilidade específica.

        Args:
            hab_procurada (str): A habilidade a ser procurada.

        Returns:
            str: Uma string contendo as raças e habilidades correspondentes encontradas.
        """
        self.cursor.execute('SELECT nome_raca, hab_raciais FROM racas')

        lista_habs = []
        infos = []
        consulta = self.cursor.fetchall()
        for habs in consulta:
            raca = habs[0]
            habilidades = habs[1].split(', ')
            if hab_procurada in habilidades:
                habilidades.remove(hab_procurada)
                habilidades.insert(0, hab_procurada)
                t = f''' Raça: {raca}, Habilidades: {', '.join(habilidades)} '''
                infos.append(t)

        

        info = '\n'.join(infos)

        return info
    
    def buscar_habilidade_subraca(self, hab_procurada):
        self.cursor.execute('SELECT nome_subraca, hab_subraca FROM subracas')


        infos = []
        consulta = self.cursor.fetchall()
        for habs in consulta:
            subraca = habs[0]
            habilidades = habs[1].split(', ')
            if hab_procurada in habilidades:
                habilidades.remove(hab_procurada)
                habilidades.insert(0, hab_procurada)
                t = f''' Raça: {subraca}, Habilidades: {', '.join(habilidades)} '''
                infos.append(t)

        info = '\n'.join(infos)

        return info
    
    def visualizar_classe(self, classe):
        """Visualiza as informações de uma classe específica.

        Args:
            classe (str): O nome da classe a ser visualizada.

        Returns:
            str: Uma string formatada contendo as informações da classe.
        """
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

Sub-Classes:
{self.buscar_subclasses(classe)}
 '''
        
        return t
    
    def buscar_subclasses(self, classe):
        self.cursor.execute(f'SELECT nome_subclasse FROM subclasses INNER JOIN classes ON classes.id_classe = subclasses.id_classe WHERE nome_classe = "{classe}"')

        info = []
        consulta = self.cursor.fetchall()
        for subclasse in consulta:
            info.append(subclasse[0])

        return '\n'.join(info)

    def visualizar_habs_raca(self, raca):
        """Visualiza as habilidades de uma raça específica.

        Args:
            raca (str): O nome da raça a ser visualizada.

        Returns:
            str: Uma string formatada contendo as habilidades da raça.
        """
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