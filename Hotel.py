print('Óla, seja bem vindo ao Hotel')

print('precisamos de seus dados')
cliente_1 = str(input('Nome por favor: '))                            
idade_1 = int(input('Sua Idade por favor: '))              
diaria_1 = int(input('Quantos dias pretende ficar: ')) 
pessoas_1 = int(input('Quantas pessoas serão hospedadas: '))

if pessoas_1 == 3 or pessoas_1 < 3:

    print(f'''temos 3 estadías sendo :

    SIMPLES - R$ 100.00 por dia
    DUPLO - R$ 150.00 por dia
    LUXO -R$ 250.00 por dia
    ''')

    Simples = 100.00
    Duplo = 150.00
    Luxo = 250.00
  
    soma_1 = diaria_1 + pessoas_1
    simples_1 = soma_1 * Simples
    soma_2 = diaria_1 + pessoas_1
    duplo_1 = soma_2 * Duplo
    soma_3 = diaria_1 + pessoas_1
    luxo_1 = soma_3 * Luxo

    quarto = str(input('Pretende ficar em qual quarto?: '))
    if quarto == 'Simples':
         print(cliente_1,'o preço será',simples_1)
         print('Pretende pagar como?')
         escolha_1 = int(input(f'''
         Débito: 1
         Crédito: 2
         -> '''))
         if escolha_1 == 1:
            print('Débito né?, vamos continuar')
            print('Pagamento feito com sucesso!')
            print(cliente_1,'Tenha um ótimo descanço!')
        
         elif escolha_1 == 2:
            print('Crédito né?, vamos continuar')
            print('Pagamento feito com sucesso!')
            print(cliente_1,'Tenha um ótimo descanço!') 
    
    elif quarto == 'Duplo':
        print(cliente_1,'o preço será',duplo_1)
        print('Pretende pagar como?')
        escolha_2 = int(input(f'''
        Débito: 1
        Crédito: 2
        -> '''))
        if escolha_2 == 1:
            print('Débito né?, vamos continuar')
            print('Pagamento feito com sucesso!')
            print(cliente_1,'Tenha um ótimo descanço!')
        
        elif escolha_2 == 2:
            print('Crédito né?, vamos continuar')
            print('Pagamento feito com sucesso!')
            print(cliente_1,'Tenha um ótimo descanço!') 


    elif quarto == 'Luxo':
        print(cliente_1,'o preço será',luxo_1)
        print('Pretende pagar como?')
        escolha_3 = int(input(f'''
        Débito: 1
        Crédito: 2
        -> '''))  
        if escolha_3 == 1:
            print('Débito né?, vamos continuar')
            print('Pagamento feito com sucesso!')
            print(cliente_1,'Tenha um ótimo descanço!')
        
        elif escolha_3 == 2:
            print('Crédito né?, vamos continuar')
            print('Pagamento feito com sucesso!')
            print(cliente_1,'Tenha um ótimo descanço!') 
    
else:
    print(cliente_1,'A quantidade máxima permitida é 3, volte ao inicio. ')
