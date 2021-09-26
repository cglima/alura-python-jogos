import random


def jogar():
    print(20 * "=")
    print(f"Jogo de adivinhação: {__name__}")
    print(20 * "=")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade? ")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível do jogo: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = int(input("Digite um número entre 1 e 100: "))
        print("você digitou o número", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Parabéns! Você acertou o número secreto e fez {} pontos".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto")
                if rodada == total_de_tentativas:
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto")
                if rodada == total_de_tentativas:
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))

    print(20 * "=")
    print("Fim de jogo")
    print(20 * "=")

#print(f"Oi, eu sou o modulo adivinhação e meu nome é: {__name__}")


if __name__ == "__main__":
    jogar()

