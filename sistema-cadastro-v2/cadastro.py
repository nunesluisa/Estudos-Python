from database import conectar
def cadastrar_pessoa (nome,idade,cidade,urgencia, data_abertura):
    conexao = conectar ()
    cursor = conexao.cursor()

    cursor.execute (
        '''
        INSERT INTO pessoas (
            nome,
            idade,
            cidade,
            urgencia,
            data_abertura
        )
        VALUES (?,?,?,?,?)
        ''',
        (nome,idade,cidade,urgencia,data_abertura)
    )
    conexao.commit ()
    conexao.close ()
def listar_cadastro ():
    conexao = conectar ()
    cursor= conexao.cursor()

    cursor.execute ('SELECT * FROM pessoas')

    pessoas = cursor.fetchall()

    conexao.close()
    return pessoas