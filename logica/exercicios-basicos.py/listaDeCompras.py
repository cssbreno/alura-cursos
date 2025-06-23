import os

mensagem = 'Sua lista está vazia. Adicione itens nela: '
lista_De_Compras = [input(mensagem)]
print(lista_De_Compras)

while True:
    opcao = input('O que deseja fazer: '
                  '[1] - Adicionar item'
                  ', [2] - Remover item'
                  ', [3] - Listar compras: ')
    
    if opcao == '1':
        os.system('clear')
        objeto = input('Informe o item a ser adicionado: ')
        lista_De_Compras.append(objeto)
        print('Item adicionado na lista', lista_De_Compras)

    elif opcao == '2':
        indice = int(input('Informe o numero do item na lista: '))

        try:
            del lista_De_Compras[indice]
            print('Item removido da lista', lista_De_Compras)

        except IndexError:
            print('Não foi possivel apagar o item informado')

    elif opcao == '3':
        print('Sua lista de compras é: ', lista_De_Compras)

    else:
        print('Você não digitou uma opção válida!')
