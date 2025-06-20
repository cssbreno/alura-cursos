iniciar_jogo = input('Vamos jogar? (S)im / (N)ão: ').lower().startswith("s")

palavra_secreta = 'Python'

try:
    if iniciar_jogo is True:
        print('No jogo, você deve tentar adivinhar a palavra secreta.\
            Vamos lá!')
        print('------------------------')
        
        palavra_oculta = ['*' for _ in palavra_secreta]
        print('A palavra secreta é: ' + ''.join(palavra_oculta))

        while True:
            chute_do_usuario = input('Digite uma letra: ').lower()
            for i,letra in enumerate(palavra_secreta):
                if chute_do_usuario == letra.lower():
                    palavra_oculta[i] = letra
                    print('A palavra secreta é: ' + ''.join(palavra_oculta))
            continue

except ValueError:
    print('Tudo bem. Até a próxima!')