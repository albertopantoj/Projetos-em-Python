#Crie um jogo em que o computador escolhe um número aleatório de 1 a 100. 
# O usuário tem 7 tentativas para acertar, e o jogo deve dar dicas: "maior" ou "menor".

from random import choice
print("Olá, você está participando de um game agora!")
print("Seja bem vindo(a)")
print("O computador escolherá um número de 1 a 100, e você terá até 7 chances para acertar")
numeros = list(range(1, 100+1))
computador_escolha = choice(numeros)
escolha = 0
while True:
    escolha_jogador = int(input("Escolha um número: \n"))
    escolha += 1
    if escolha_jogador != computador_escolha and escolha <= 7:
        print("Você errou! Tente novamente")
    elif escolha > 7:
        print("Game Over! Você perdeu todas as chances")
        break
    else:
        print("Você acertou! Parabéns!")
        break
print("FIM!")