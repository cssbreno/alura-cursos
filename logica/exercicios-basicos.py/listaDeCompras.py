import os

mensagem = 'Sua lista está vazia. Adicione itens nela: '
lista_De_Compras = []

print(mensagem)
itens_iniciais = input('Digite os itens (separados por vírgula): ')
# Separa os itens por vírgula e remove espaços em branco
itens_separados = [item.strip() for item in itens_iniciais.split(',')]
lista_De_Compras.extend(itens_separados)

print('Lista inicial:', lista_De_Compras)

while True:
    opcao = input('O que deseja fazer: '
                  '[1] - Adicionar item'
                  ', [2] - Remover item'
                  ', [3] - Listar compras: ')

    if opcao == '1':
        os.system('clear')
        novos_itens = input('Digite os itens (separados por vírgula): ')
        # Separa os itens por vírgula e remove espaços em branco
        itens_separados = [item.strip() for item in novos_itens.split(',')]
        lista_De_Compras.extend(itens_separados)
        print('Itens adicionados na lista:', lista_De_Compras)

    elif opcao == '2':
        indice = int(input('Informe o numero do item na lista: '))

        try:
            del lista_De_Compras[indice]
            print('Item removido da lista', lista_De_Compras)

        except IndexError:
            print('Não foi possivel apagar o item informado')

        except ValueError:
            print('Item não está presente na lista')

        except Exception:
            print('Verifique e tente novamente')

    elif opcao == '3':
        if len(lista_De_Compras) <= 0:
            print('Lista vazia')
        else:
            print('Sua lista de compras é:')

            for item, nome in enumerate(lista_De_Compras):
                print(f'{item} - {nome}')

    else:
        print('Você não digitou uma opção válida!')
