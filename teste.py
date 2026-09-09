print ('======= MERCADO DA LULU ========')
nomecli = (input('digite o nome do cliente: '))
nomepro = (input('digite o nome do produto: '))
preçouni = float (input('digite o valor do produto: '))
quanti = int (input('digite a quantidade comprada: '))
print ('=======RESUMO DA COMPRA==========')
print ('cliente: ', nomecli)
print ('produto: ', nomepro)
print ('quantidade: ', quanti)
print ('Total: ', (preçouni*quanti))
total = preçouni*quanti
if total < 100:
    print ('sem desconto')
elif 100 <= total < 299.99:
    print ('você teve um desconto de 10 reais')
    totalfim = total - 10
    print ('o valor a ser pago é de ', totalfim)
elif total >= 300:
    print ('desconto de 30 reais')
    totalfim = total - 30 
    print ('o valor a ser pago é de ', totalfim)
formapag = int (input ('escolha sua forma de pagamento, 1 - pix, 2- dinheiro, 3 - cartão: '))
if formapag == 1:
    print ('você ganhou mais 5 reais de desconto')
    print ('total a pagar: ', (totalfim - 5))
elif formapag == 2:
    print ('Sem desconto, o total a ser pago é de: ', totalfim)
elif formapag == 3:
    print ('sem desconto, o total a ser pago é de: ', totalfim)