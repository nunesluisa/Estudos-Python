# Sistema de cadastro e gerenciamento
print ('==========SISTEMA DE CADASTRO==========')
print ('1 - Cadastrar a pessoa \n 2 - Listar cadastros \n 3 - Buscar cadastro \n 0 - Sair')
opção = int (input ('Escolha uma opção: '))
if opção == 1:
    nome = input ('Digite o nome:')
    idade = int(input ('Digite a idade: '))
    cidade = input ('Qual a cidade: ')
    print ('Os dados cadastrados são: \n', nome, '\n', idade, '\n', cidade, '\n' )
