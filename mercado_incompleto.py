# Crie um sistema de e-commerce, onde o usuário possa cadastrar-se, comprar um produto, descobrir o valor total e pagar

login = 'Gabriel'
senha = '123'
meu_login = str(input('Digite seu login: '))
minha_senha = str(input('Digite sua senha: '))

if meu_login == login and minha_senha == senha:   
    print('Login feito com sucesso')
    categoria = ['Mangás','Jogos','Comidas']
    mangas_cat = ['Bleach','Dragon Ball','Naruto']  
    jogos_cat = ['Rummikub','Ludo','Monopoly']
    comida_cat = ['Arroz','Feijão','Macarrão']
    val_manga_cat = [12.00 , 15.00 , 10.00]
    val_jogo_cat = [30.00 , 25.00 , 50.00]
    val_comida_cat = [20.00 , 5.30 , 7.00]
    carrinho = []

    print(f'''Escolha uma categoria:

    0 - Mangás
    1 - Jogos
    2 - Comidas
    ''')

    escolha = int(input('-> '))
    if escolha == 0:
        print(f'''

        0 - Bleach - R$ 12.00
        1 - Dragon ball - R$ 15.00
        2 - Naruto - R$ 10.00
        ''')

        print('Ótimo, deseja escolher quem?')
    sistema = str(input('-> '))
    if sistema == 0:
       print('Bleach - R$ 12.00')
       carrinho +=('Bleach - R$12.00')    
    elif sistema == 1:
        print('Dragon ball - R$ 15.00') 
    else:
        print('Naruto - R$ 10.00')

    #----------------------------------------------------
    if escolha == 1:
        print(f'''

        0 - Rummikub - R$ 30.00
        1 - Ludo - R$ 25.00
        2 - Monopoly - R$ 50.00
        ''')

    print('Ótimo, deseja escolher quem?')
    sistema1 = str(input('-> '))
    if sistema1 == 0:
       print('Rummikub - R$ 30.00')    
    elif sistema1 == 1:
        print('Ludo - R$ 25.00') 
    else:
        print('Monopoly - R$ 50.00')    
    #----------------------------------------------------     
    if escolha == 2:
        print(f'''
        
        0 - Arroz - R$ 20.00
        1 - Feijão - R$ 5.30
        2 - Macarrão - R$ 7.00
        ''')

        print('Ótimo, deseja escolher quem?')
    sistema2 = str(input('-> '))
    if sistema2 == 0:
       print('Arroz - R$ 20.00')    
    elif sistema2 == 1:
        print('Feijão - R$ 5.30') 
    else:
        print('Macarrão - R$ 7.00')    
    #-----------------------------------------------------    
    print('Ótimo, deseja escolher quem?')
    sistema = str(input('-> '))
    if sistema == 0:
       print()    
    if sistema == 1:
       print() 
    if sistema == 2:
       print()    

    

elif meu_login != login or minha_senha != senha:
    print('Algo está errado, tente novamente')



