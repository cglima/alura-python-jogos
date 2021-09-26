import forca
import adivinhacao

# print(f"Oi, eu sou o modulo jogos e meu nome é: {__name__}")

print(31 * "*")
print(5 * "*", "Escolha o seu jogo!", 5 * "*")
print(31 * "*")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogando Forca")
    forca.jogar()
elif jogo == 2:
    print("Jogando adivinhação")
    adivinhacao.jogar()
