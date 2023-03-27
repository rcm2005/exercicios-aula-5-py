nome = input('Digite seu nome: ')
fixo = 2500
carros_v = int(input('Digite quantos carros você vendeu: '))
comissao = 200 * carros_v

extra = 2/100 * 300000

total = extra + fixo + comissao

print(f'O salário total de {nome} é {total}')



