def jogar():
    print(20 * "*")
    print("***Bem vindo ao jogo da Forca!***")
    print(20 * "*")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not acertou and not enforcou):

        chute = input("Qual a letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                print("Encontrei a letra {} na posição {}".format(letra, index))
                index = index + 1

        print("Jogando...")

    print(20 * "=")
    print("Fim de jogo")
    print(20 * "=")


if __name__ == "__main__":
    jogar()