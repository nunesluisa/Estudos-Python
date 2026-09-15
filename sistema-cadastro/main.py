# Sistema de cadastro e gerenciamento
import json
with open ('sistema-cadastro/dados.json', 'r', encoding = 'utf-8') as arquivo:
    pessoas = json.load (arquivo)
while True:
    print ('==========SISTEMA DE CADASTRO==========')
    print ('1 - Cadastrar a pessoa \n 2 - Listar cadastros \n 3 - Buscar cadastro \n 4 - Remover cadastro \n 5 - Lista de atendimentos \n 6 - Atender proximo ticket \n 7 - Editar cadastro \n 0 - Sair')
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
        with open ('sistema-cadastro/dados.json', 'w', encoding = 'utf-8') as arquivo:
            json.dump (pessoas, arquivo, ensure_ascii=False)
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
                with open ('sistema-cadastro/dados.json', 'w', encoding = 'utf-8')as arquivo:
                    json.dump (pessoas,arquivo, ensure_ascii= False)
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
    elif opção == 6:
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
        if len(fila)==0:
            print ('A fila está vazia')
        else:
            print ('O próximo da fila é', fila [0]['nome'])
            pessoas.remove (fila[0])
            with open ('sistema-cadastro/dados.json', 'w', encoding = 'utf-8') as arquivo:
                json.dump(pessoas, arquivo, ensure_ascii= False)
    elif opção == 7:
        editar = input ('Qual cadastro você deseja editar? ')
        achou = False
        for pessoa in pessoas:
            if pessoa ['nome'].lower () == editar.lower ():
                print ('1 - Nome \n 2 - Idade \n 3 - Cidade \n 4 - Urgência \n')
                pessoa_editar = int (input('O que você deseja editar? Digite: 0 para voltar ao menu anterior '))
                if pessoa_editar == 1:
                    novo_nome = input ('Qual o novo nome? ')
                    pessoa ['nome'] = novo_nome
                    print ('Você acabou de editar o nome para', novo_nome)
                elif pessoa_editar == 2 :
                    idade_nova = int (input ('Qual a nova idade? '))
                    pessoa ['idade'] = idade_nova
                    print ('Você acabou de editar a idade para', idade_nova)
                elif pessoa_editar == 3:
                    cidade_nova = input ('Qual a nova cidade ?')
                    pessoa ['cidade'] = cidade_nova
                    print ('você acabou de editar a cidade para', cidade_nova)
                elif pessoa_editar == 4:
                    urgencia_nova = input ('Qual a urgência a ser atualizada? ')
                    pessoa ['urgencia'] = urgencia_nova
                    print ('você acabou de editar a urgêrcia para', urgencia_nova)
                with open ('sistema-cadastro/dados.json', 'w', encoding= 'utf-8') as arquivo: 
                    json.dump (pessoas, arquivo, ensure_ascii= False)
    elif opção == 0:
        print ('Você encerrou o cadastro!')
        break 
    else:
        print ('Opção invalida! Por favor digite uma das opções')
