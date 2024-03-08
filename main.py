import sqlite3

conn = sqlite3.connect('rpg.db')

cursor = conn.cursor()

raca = 'Aarakocra'

cursor.execute(f"SELECT nome_raca, descricao, idade, velocidade, alinhamento, medidas, hab_raciais FROM racas WHERE nome_raca = '{raca}'")

info = cursor.fetchall()[0]

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

print(t)