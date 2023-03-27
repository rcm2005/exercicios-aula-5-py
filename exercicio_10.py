numero = int(input('numero 3 digitos: '))

a = numero // 100
resto = numero % 100
b = resto // 10
c = resto % 10

print(f'Numero invertido: {c}{b}{a}')


centena = num//100
dez = (num%100)//10
unidade = num%10

