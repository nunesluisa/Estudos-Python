from datetime import datetime
from database import criar_tabela
from cadastro import cadastrar_pessoa, listar_cadastro
from validacoes import validar_nome, validar_idade, validar_urgencia

criar_tabela ()
while True:
    print('\n===== SISTEMA DE CADASTRO V2 =====')
    print('1 - Cadastrar pessoa')
    print('2 - Listar cadastros')
    print('0 - Sair')

    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print('Digite somente números')
        continue

    if opcao == 1:
        nome = validar_nome()
        idade = validar_idade()
        cidade = input('Digite a cidade: ')
        urgencia = validar_urgencia()

        data_abertura = datetime.now().strftime('%d/%m/%Y %H:%M')

        cadastrar_pessoa(
            nome,
            idade,
            cidade,
            urgencia,
            data_abertura
        )

        print('Cadastro realizado com sucesso')

    elif opcao == 2:
        pessoas = listar_cadastro()

        for pessoa in pessoas:
            print('Ticket:', pessoa[0])
            print('Nome:', pessoa[1])
            print('Idade:', pessoa[2])
            print('Cidade:', pessoa[3])
            print('Urgência:', pessoa[4])
            print('Data de abertura:', pessoa[5])
            print('Data de atendimento:', pessoa[6])
            print('----------------------')

    elif opcao == 0:
        print('Programa encerrado')
        break

    else:
        print('Opção inválida')
