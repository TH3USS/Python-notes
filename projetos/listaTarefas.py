lista = []

while True:

    escolha = input('selecione (1/2/3): ')

    if escolha == '1':
        if lista == []:
            print('lista vazia')
        else:
            print(lista)

    elif escolha == '2':
        print('adicione um item: ')
        add = input('escreva o dado a ser adicionado')
        lista.append(add)



    elif escolha == '3':
        break

    else:
        print('opção invalida')




    break