# Crie um jogo simples que gere números inteiros aleatórios entre 1-20.
# Que o programa verifique se o valor inserido pelo usuario é igual ao aleatório.
# O programa será repetido 5 vezes. 
# O programa deverá ser encerrado caso nao digite um numero dentro do intervalo. 
# Mostrar uma mensagem ao usuario caso ele digite um numero diferente do aleatorio.
# Se o usuario nao digitar um numro maior ou menor que o numero aleatorio, que seja avisado.
# O usuario acertando o numero aleatorio, no final será mostrado a quantidade de acertos.



from random import randint      

chances = 0

for numero in range(1, 6):
    print(f'Jogada {numero}')
    aleatorio = randint(1, 20)
    usuario = int(input("Escolha um numero de 1 - 20: "))

    if usuario in range(1, 21):
        if usuario > aleatorio:
            print("Tente um numero menor que o aleatorio!")
            print(f'Numero aleatorio: {aleatorio}')
        
        elif usuario < aleatorio:
            print("Tente um numero menor que o aleatorio!")
            print(f'Numero aleatorio: {aleatorio}')
        
        else:
            print("voce acertou!")
            chances +=1 
        
    else:
        print("FIM")
        break

print(f'acertos:  {chances}')


