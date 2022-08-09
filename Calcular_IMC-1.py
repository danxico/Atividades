rodando = True

while rodando:
    nome = input('Digite o seu nome: ')
    idade = input('Digite a sua idade: ')
    peso = input('Digite o seu peso: ')
    altura = input('Digite a sua altura: ')

    try:
        imc = float(peso) / float(altura) ** 2
        print('\nO IMC de ' + nome + ' é ' + str(imc))
    except:
        print('\nCaractere inválido! Use somente ponto e números')

    resp = input('\nDeseja continuar? (sim/não): ')

    if resp[0].lower() == 'n':
        print('Você encerrou a aplicação.')
        break
