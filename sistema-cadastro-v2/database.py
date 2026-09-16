import sqlite3
def conectar ():
    conexao = sqlite3.connect ('sistema-cadastro-v2/sistema.db')
    return conexao

def criar_tabela ():
    conexao = conectar ()
    cursor = conexao.cursor()

    cursor.execute ('''
    CREATE TABLE IF NOT EXISTS pessoas (
        ticket INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        cidade TEXT NOT NULL,
        urgencia TEXT NOT NULL,
        data_abertura TEXT NOT NULL,
        data_atendimento TEXT
        )
''')

    conexao.commit()
    conexao.close()