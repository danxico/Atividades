rodando = True


def calcular(num1, op, num2):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*' or op == 'x':
        result = num1 * num2
    elif op == '/':
        if num1 != 0:
            result = num1 / num2
        else:
            return 'É impossível dividir por zero'
    else:
        print('\nOperação não é válida')
    return result


while rodando:
    print('\n---------- Calculadora ----------')
    numero1 = input('Digite o primeiro numero: ')
    operador = input('Digite a operação (+, -, / ou *): ')
    numero2 = input('Digite o segundo numero: ')

    try:
        num2 = float(numero2)
        num1 = float(numero1)
        result = calcular(num1, operador, num2)
        print('\n', numero1, operador, numero2 + ' = ' + str(result))
    except:
        print('\nCaractere inválido!')

    resposta = input('\nDeseja continuar? (sim/não): ')
    if resposta[0].lower() == 'n':
        print('Você encerrou a calculadora')
        break
