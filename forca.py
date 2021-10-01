def jogar():
    print(33 * "*")
    print("***Bem vindo ao jogo da Forca!***")
    print(33 * "*")

    palavra_secreta = "banana".upper()
    #list comprehenshion
    letras_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = input("Qual a letra? ")
        chute = chute.strip().upper()


        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += + 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)


    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print(20 * "=")
    print("Fim de jogo")
    print(20 * "=")


if __name__ == "__main__":
    jogar()