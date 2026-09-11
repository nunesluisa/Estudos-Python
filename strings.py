pessoas = []
continuar = "sim"
while continuar == "sim":
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    cidade = input('Qual a cidade: ')

    pessoa = { 'nome': nome,
        'idade': idade,
        'cidade': cidade
    }
    (pessoas.append(pessoa))
    continuar = input ('você deseja continuar? Sim ou Não: ').strip().lower()
print (pessoas)

