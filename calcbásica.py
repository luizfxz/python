n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

s = str(input('Escolha uma operação para ser realizada: ( + / - / * / / )' '\n'))

if s == '+':
    res = n1 + n2
    print(f'A soma entre {n1} + {n2} é: {res}')
elif s == '-':
    res = n1 - n2
    print(f'A subtração entre {n1} - {n2} é: {res}')
elif s == '*':
    res = n1 * n2
    print(f'A multiplicação entre {n1} x {n2} é: {res}')
elif s == '/':
    res = n1 / n2
    print(f'A divisão entre {n1} / {n2} é: {res}')
