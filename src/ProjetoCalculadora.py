while True:
    operacao = input('Qual operação você deseja fazer (+, -, *, /) ou \'q\' para sair? ')
    if operacao == 'q':
        break
    elif operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
        num1 = int(input('Digite o número 1:'))
        num2 = int(input('Digite o número 2:'))
    else:
        print('Operação Inválida')

    if operacao == '+':
        total = num1 + num2
        print(total)
    elif operacao == '-':
        total = num1 - num2
        print(total)
    elif operacao == '*':
        total = num1 * num2
        print(total)
    elif operacao == '/':
        total = num1 / num2
        print(total)


