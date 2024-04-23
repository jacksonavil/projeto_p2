# for cont_ext in range(1,6):
#     print(f'\nRodada: {cont_ext}')
#     for cont_int in range(5, 0, -1):
#         print(f'valor: {cont_int}')
# print('Fim do laço')

# ----------------------------------------------

import random
for a in range(1,6):
    print(f'\nConjunto {a}')
    for b in range(5):
        num = random.randint(1,100)
        print(f'valor: {num}')
        