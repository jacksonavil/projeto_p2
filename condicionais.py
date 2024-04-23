# Tipos ( simples, comporto, encadeado)

# n1 = n2 = 0.0
# media = 0.0

# n1 = float(input('Digite a primeira nota:'))
# n2 = float(input('Digite a segunda nota:'))

# media = (n1 + n2) / 2

# if (media >=7):
#     print("Resultado Aprovado!")
#     print("parabens")
# elif(media >=5):
#     print('Voce está de recuperacao')
# else:
#     print('Aluno Reprovado...')

# print('Sua média é {}' .format(media))


n1 = n2 = n3 = 0.0
media = 0.0

n1 = float(input('Digite a primeira nota'))
n2 = float(input('Diite a segunda nota'))
n3 = float(input('Digite a terceira nota'))

media = (n1+n2+n3)/3

if(media >=7):
    print("Resultado Aprovado")
    print("Parabens")
elif(media >=5):
    print("Vc esta em recuperação")
    print("Atenão")
else:
    print("Reprovado")

print('Sua media é {}' .format(media))


# lista = [0, 1, 0, 1, 0, 0, 1, 0, 1]
# c = 0

# for i in range(len(lista)):
#     if lista[i] == 0:
#         #print("Lâmpada com defeito")
#         c += 1
#     else:
#         print("Lâmpada funcionando")

# quant_lamp_ok = len(lista) - c
# _tx_naook = c/len(lista) * 100

# print(f"\nquantidade de lampadas {quant_lamp_ok} e que não existe {c}, tx {_tx_naook}%")

