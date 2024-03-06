import sqlite3

conn = sqlite3.connect('rpg.db')

cursor = conn.cursor()

cursor.execute(''' CREATE TABLE tabela_racas
                    (id_raca INTEGER PRIMARY KEY, nome_raca VARCHAR(50), descricao TEXT, alinhamento TEXT, medidas TEXT, hab_raciais TEXT) ''')






    

conn.commit()
conn.close()