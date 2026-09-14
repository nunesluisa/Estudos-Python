# Sistema de cadastro e gerenciamento
pessoas = []
while True:
    print ('==========SISTEMA DE CADASTRO==========')
    print ('1 - Cadastrar a pessoa \n 2 - Listar cadastros \n 3 - Buscar cadastro \n 4 - Remover cadastro \n 5 - Lista de atendimentos \n 0 - Sair')
    opção = int (input ('Escolha uma opção: '))
    if opção == 1:
        nome = input ('Digite o nome:')
        idade = int(input ('Digite a idade: '))
        cidade = input ('Qual a cidade: ')
        while True: 
            urgencia = int (input('Qual a urgência do atendimento?\n 1 - baixa \n 2 - média \n 3 - alta: '))
            if urgencia == 1:
                urgencia = 'baixa'
                break
            elif urgencia == 2:
                urgencia = 'média'
                break
            elif urgencia == 3:
                urgencia = 'alta'
                break
            else:
                print ('Opção invalida')
        pessoa= {
            'nome': nome,
            'idade': idade,
            'cidade': cidade,
            'urgencia': urgencia
        }
        pessoas.append (pessoa)
        print ('Os dados cadastrados são: \n', nome, '\n', idade, '\n', cidade, '\n', urgencia, '\n' )
    elif opção == 2:
        print ('Acessando cadastro...')
        print ('------------------')
        if len (pessoas) == 0:
            print ('Não tem pessoas cadastradas \nVoltando ao inicio')
        else:
            for pessoa in pessoas:
                print (pessoa ['nome'])
                print (pessoa ['idade'])
                print (pessoa ['cidade'])
                print (pessoa ['urgencia'])
                print ( '--------------------')
    elif opção == 3:
        busca = input ('Qual o nome você deseja buscar: ')
        encontrou = False
        for pessoa in pessoas:
            if pessoa ['nome'].lower() == busca.lower ():
                print ('Achamos o cadastro correspondente')
                print ('-----------------')
                print (pessoa ['nome'])
                print (pessoa ['idade'])
                print (pessoa ['cidade'])
                print (pessoa['urgencia'])
                print ('----------------')
                encontrou = True
        if encontrou == False:
            print('Não foram encontrados dados')
    elif opção == 4:
        remove = input ('Qual nome você deseja remover? ')
        removeu = False
        for pessoa in pessoas:
            if pessoa ['nome'].lower () == remove.lower():
                pessoas.remove(pessoa)
                print ('Você acabou de remover do cadastro', pessoa ['nome'])
                removeu = True
        if removeu == False:
            print ('Não achamos esse cadastro para remover')
    elif opção == 5:
        print ('Fila de atendimento: ')
        print ('---------------')
        prioridades = {
            'alta': 3,
            'média': 2,
            'baixa': 1
        }
        fila = sorted (
            pessoas,
            key=lambda pessoa: prioridades[pessoa['urgencia']],
            reverse=True
        )
        for numero, pessoa in enumerate (fila, start = 1):
            print ('TICKET', numero, '-', pessoa ['nome'], 'A Urgência do atendimento é - ', pessoa ['urgencia'])
    elif opção == 0:
        print ('Você encerrou o cadastro!')
        break 
    else:
        print ('Opção invalida! Por favor digite uma das opções')
