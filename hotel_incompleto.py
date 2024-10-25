
print('Óla, seja bem vindo ao Hotel')
print('precisaremos de seus dados')
cliente_1 = str(input('Nome porfavor: '))                 #          | 
idade_1 = int(input('Sua Idade porvavor: '))              # Cliente 1|
diaria_1 = int(input('Quantos dias pretende ficar: '))    #          |
print(f'''temos 3 estadías sendo :

SIMPLES - R$ 100.00 por dia
DUPLO - R$ 150.00 por dia
LUXO -R$ 250.00 por dia
''')

Simples = 100.00
Duplo = 150.00
Luxo = 250.00
  
soma_1 = diaria_1 * Simples
soma_2 = diaria_1 * Duplo
soma_3 = diaria_1 * Luxo

quarto = str(input('Pretende ficar em qual quarto?: '))
if quarto == 'Simples':
    print(soma_1)
    
elif quarto == 'Duplo':
    print(soma_2)
    
elif quarto == 'Luxo':
    print(soma_3)    
    
else:
    ('A quantidade máxima permitida é 3 ')
