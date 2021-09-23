print(20 * "=")
print("Jogo de adivinhação")
print(20 * "=")

numero_secreto = 5
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute = int(input("Digite um número: "))
    print("você digitou o número", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou o número secreto")
    else:
        if (maior):
            print("Você errou! O seu chute é maior que o número secreto")
        elif(menor):
            print("Você errou! O número digitado é menor que o número secreto")

    rodada = rodada +1

print(20 * "=")
print("Fim de jogo")
print(20 * "=")