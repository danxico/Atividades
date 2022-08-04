
rodando = True

while rodando:
    numero = input('Digite um numero: ')
    print('------- TABUADA DO ' + str(numero) + ' -------')
    for i in range(11):
        result = int(numero) * i
        print(str(numero) + ' X ' + str(i) + ' = ' + str(result))
