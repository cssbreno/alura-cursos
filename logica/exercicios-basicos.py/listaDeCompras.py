mensagem = 'Sua lista está vazia. Adicione itens nela: '
lista_De_Compras = [input(mensagem)]
print(lista_De_Compras)

while True: 
    if lista_De_Compras != '':
        opcao = input('O que deseja fazer: '
                      '[1] - Adicionar item'
                      ', [2] - Remover item'
                      ', [3] - Listar compras: ')
        
        if opcao == '1':
            objeto = input('Informe o item a ser adicionado: ')
            lista_De_Compras.append(objeto)
            print('Item adicionado na lista', lista_De_Compras)

        elif opcao == '2':
            print('Itens na lista:')
            for i, item in enumerate(lista_De_Compras):
                print(f'{i}: {item}')
            
            try:
                indice = int(input('Informe o numero do item na lista: '))
                if 0 <= indice < len(lista_De_Compras):
                    item_removido = lista_De_Compras.pop(indice)
                    print(f'Item "{item_removido}" removido da lista', 
                          lista_De_Compras)
                else:
                    print('Índice inválido!')
            except ValueError:
                print('Digite um número válido!')

        elif opcao == '3': 
            print('Sua lista de compras é: ', lista_De_Compras)

        else: 
            print('Você não digitou uma opção válida!')
            continue