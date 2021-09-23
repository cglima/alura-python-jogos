print(20 * "=")
print("Jogo de adivinhação")
print(20 * "=")

numero_secreto = 5
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute = int(input("Digite um número entre 1 e 100: "))
    print("você digitou o número", chute)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou o número secreto")
        break
    else:
        if (maior):
            print("Você errou! O seu chute é maior que o número secreto")
        elif(menor):
            print("Você errou! O número digitado é menor que o número secreto")

print(20 * "=")
print("Fim de jogo")
print(20 * "=")