def validar_nome ():
    while True:
        nome = input ('Digite seu nome: ')
        if nome.replace ('','').isalpha:
            return nome
        else:
            print ('Por favor, digite somente letras')
def validar_idade():
    while True:
        try:
            idade = int(input('Digite a idade: '))
            return idade
        except ValueError:
            print ('Por favor digite somente números')
def validar_urgencia (): 
    while True:
        try:
            urgencia = int(input(
                'Qual a urgência do atendimento?\n'
                '1 - baixa\n'
                '2 - média\n'
                '3 - alta\n'
                'Escolha: '
            ))

            if urgencia == 1:
                return 'baixa'

            elif urgencia == 2:
                return 'média'

            elif urgencia == 3:
                return 'alta'

            else:
                print('Opção inválida')

        except ValueError:
            print('Digite somente números')