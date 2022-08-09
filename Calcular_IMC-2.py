def classificar(valor_imc):
    if valor_imc < 18.5:
        classe = 'Abaixo peso'
    elif 18.5 <= valor_imc < 25:
        classe = 'Peso normal'
    elif 25 <= valor_imc < 30:
        classe = 'Sobrepeso'
    else:
        classe = 'Obesidade'
    return classe


rodando = True

while rodando:
    nome = input('Digite o seu nome: ')
    idade = input('Digite a sua idade: ')
    peso = input('Digite o seu peso: ')
    altura = input('Digite a sua altura: ')

    try:
        imc = float(peso) / float(altura) ** 2
    except:
        print('\nCaractere inválido! Use somente ponto e números')

    print('\nO IMC de ' + nome + ' é: ' + str(imc) + ' e a classificação: ' + str(classificar(imc)))

    resp = input('\nDeseja continuar? (sim/não): ')
    if resp[0].lower() == 'n':
        print('Você encerrou a aplicação.')
        break
