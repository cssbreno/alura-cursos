iniciar_jogo = input('Vamos jogar? (S)im / (N)ão: ').lower().startswith("s")

palavra_secreta = 'Respeito'.lower()
numero_tentativas = 0

if iniciar_jogo is True:
    print('No jogo, você deve tentar adivinhar a palavra secreta. Vamos lá!')
    print('------------------------')
    
    palavra_oculta = ['*' for _ in palavra_secreta]
    print('A palavra secreta é: ' + ''.join(palavra_oculta))

    letras_acertadas = ''

    while True:
        
        chute_do_usuario = input('Digite uma letra: ').lower()
        numero_tentativas += 1

        # Valida quantidade de letras digitadas
        if len(chute_do_usuario) > 1:
            print('Digite apenas uma letra.')
            continue

        if chute_do_usuario in palavra_secreta:
            letras_acertadas += chute_do_usuario

        palavra_completa = ''

        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_completa += letra_secreta
            else:
                palavra_completa += '*'

        print('Palavra formada: ', palavra_completa)

        if palavra_completa == palavra_secreta:
            print('Você ganhou! 🏆')
            print(f'Número de tentativas: {numero_tentativas}')
else:
    print('Tudo bem, até a próxima!')