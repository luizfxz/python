# Tabuada utilizando o while 

n1 = int(input('Digite um valor: '))

i = 0

while i <= 10:
        res = n1 * i
        print(f'{n1} x {i} = {res}')
        i = i + 1

# Tabuada utilizando o for

n1 = int(input('Digite um valor: '))

for i in range(0 , 11):
    res = n1 * i

    print(f'{n1} x {i} = {res}')
    i = i + 1

