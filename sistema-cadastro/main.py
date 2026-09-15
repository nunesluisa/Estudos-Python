# Sistema de cadastro e gerenciamento
import json
with open ('sistema-cadastro/dados.json', 'r', encoding = 'utf-8') as arquivo:
    pessoas = json.load (arquivo)
with open ('sistema-cadastro/atendidos.json', 'r', encoding = 'utf-8')as arquivo:
    atendidos = json.load (arquivo)
def listar_atendidos (atendidos):
    print ('Acessando a lista de atendidos')
    print ('-----------------')
    if len (atendidos) == 0:
            print ('Não existe ninguém atendido no momento')
    else:
        for numero, atendido in enumerate (atendidos, start=1):
            print (numero, '-', 'O atendimento foi:', atendido ['nome'])
def listar_cadastro (pessoas):
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
def buscar_cadastro (pessoas):
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
def remover_cadastro (pessoas):
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
def listar_fila (pessoas):
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
        print ('TICKET', numero, '-', pessoa ['nome'],':A urgência do atendimento é - ', pessoa ['urgencia'])
def atender_ticket (pessoas):
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
        atendidos.append (fila[0])
        pessoas.remove (fila[0])
        with open ('sistema-cadastro/dados.json', 'w', encoding = 'utf-8') as arquivo:
            json.dump(pessoas, arquivo, ensure_ascii= False)
        with open ('sistema-cadastro/atendidos.json', 'w', encoding = 'utf-8')as arquivo:
            json.dump(atendidos, arquivo, ensure_ascii= False)
def editar_cadastro (pessoas):
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
def cadastrar_pessoa (pessoas):
    nome = input ('Digite o nome:')
    while True:
        try: 
            idade = int(input ('Digite a idade: '))
            break
        except ValueError:
            print ('Idade inválida, por favor digite números')
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
while True:
    print ('==========SISTEMA DE CADASTRO==========')
    print ('1 - Cadastrar a pessoa \n 2 - Listar cadastros \n 3 - Buscar cadastro \n 4 - Remover cadastro \n 5 - Lista de atendimentos \n 6 - Atender proximo ticket \n 7 - Editar cadastro \n 8 - Listar atendidos \n 0 - Sair')
    opção = int (input ('Escolha uma opção: '))
    if opção == 1:
       cadastrar_pessoa (pessoas)
    elif opção == 2:
        listar_cadastro (pessoas)
    elif opção == 3:
        buscar_cadastro (pessoas)
    elif opção == 4:
        remover_cadastro (pessoas)
    elif opção == 5:
        listar_fila (pessoas)
    elif opção == 6:
        atender_ticket (pessoas)
    elif opção == 7:
        editar_cadastro (pessoas)
    elif opção == 8:
        listar_atendidos(atendidos)
    elif opção == 0:
        print ('Você encerrou o cadastro!')
        break 
    else:
        print ('Opção invalida! Por favor digite uma das opções')
