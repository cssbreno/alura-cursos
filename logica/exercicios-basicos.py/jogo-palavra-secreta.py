iniciar_jogo = input('Vamos jogar? (S)im / (N)ão: ').lower().startswith("s")

palavra_secreta = 'Python'

if iniciar_jogo is True:
    print('No jogo, você deve tentar adivinhar a palavra secreta. Vamos lá!')
    print('------------------------')
    
    palavra_oculta = ['*' for _ in palavra_secreta]
    print('A palavra secreta é: ' + ''.join(palavra_oculta))

    letras_acertadas = ''

    while True:
        
        chute_do_usuario = input('Digite uma letra: ').lower()

        ## Valida quantidade de letras digitadas
        if len(chute_do_usuario) > 1:
            print('Digite apenas uma letra.')
            continue

        if chute_do_usuario in palavra_secreta:
            letras_acertadas += chute_do_usuario

        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                print(letra_secreta)
            else:
                print('*')
else:
    print('Tudo bem, até a próxima!')