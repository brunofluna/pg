# Progressão geometrica 
calcular_pg = lambda x: x*2

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# função map para gerar uma lista de progressão geometríca
pg = list(map(calcular_pg, numeros))

# exibir na tela a lista da progressão geometrica
for i in pg:
    print(i)