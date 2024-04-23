# Estrutura de repetição loop
#atribuição com incremento num +1


# num = 1
# while (num <= 1000):
#     print(num)
#     num += 1          
# print('Laço encerrado')

# num = 10

# while (num =10):
#     print(num)
#     num +=1
# print('Encerrado')

nome = None
while True:
    print('Digite seu nome ou x para parar:')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'bem bindo, {nome}')
print('Ate logo')