# Menu da loja de conveniências
rep = ' ' 
while rep != 'N':

    print('---Loja de Conveniências---')
    print('------- Produtos -------')
    print('1 ----- Bolo de chocolate ---- R$ 12.00')
    print('2 ----- Pão com frango ---- R$ 8.00')
    print('3 ----- Pão com almondêga ---- R$ 9.00')
    print('---------------------------------------')

    while rep != 'S'

    prod = str(input('Escolha o código de um produto: ')) # Recebe o código do produto

    if prod != '1' and prod != '2' and prod !='3' and prod !='4': # Condição para código inválido

        print('Escolha um código válido!')

    elif prod == '1': # Condição para código do produto = 1

         quant= int(input('Digite a quantidade do produto: ')) # Solicita  a quantidade

         valorf = quant * 12.0 # Formúla para valor final

         print(f'Valor total: {valorf}') # Mostra valor final

         din = float(input('O valor da nota paga: ')) # Solicita o valor que em nota que será pago

         troco = din - valorf # Formula do troco a ser devolvido

         print(f'O valor do troco: {troco}') # Mostra o troco

    elif prod == '2': # Condição para código do produto = 2

         quant= int(input('Digite a quantidade do produto: ')) # Solicita  a quantidade

         valorf = quant * 8.0 # Formúla para valor final

         print(f'Valor total: {valorf}') # Mostra valor final

         din = float(input('O valor da nota paga: ')) # Solicita o valor que em nota que será pago

         troco = din - valorf # Formula do troco a ser devolvido

         print(f'O valor do troco: {troco}') # Mostra o troco

    elif prod == '3': # Condição para código do produto = 3

         quant= int(input('Digite a quantidade do produto: ')) # Solicita  a quantidade

         valorf = quant * 9.0 # Formúla para valor final

         print(f'Valor total: {valorf}') # Mostra valor final

         din = float(input('O valor da nota paga: ')) # Solicita o valor que em nota que será pago

         troco = din - valorf # Formula do troco a ser devolvido

         print(f'O valor do troco: {troco}') # Mostra o troco

    rep = str(input('Deseja reiniciar o programa? (S/N)')) # Reiniciação do programa
