'''
    Uma pessoa aplica o capital de R$2.100 a uma taxa de 2% ao mes durante 17 meses. Determine os juros e o montante dessa aplicação.
    J = C x i x t

    
    J = juros simples;
    c = capital incial;
    i = taxa de juros;
    t = tempo de aplicação.
'''
c = 2100
i = 2 / 100
t = 17
juros = c * i * t
print(f'Juros da aplicação: R${round(juros,2)}')
m = c + juros
print(f'Montante da aplicação: R$ {round(m,2)}')