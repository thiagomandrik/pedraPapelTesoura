import random as rd

jogadas = ["Pedra", "Papel", "Tesoura"]
jogadaComputador = rd.randint(0,2)
jogadaPlayer = 0
placarPlayer = 0
placarComputador = 0

print("########################################################")

def game():
    global jogadaPlayer
    print ("1 - Pedra")
    print ("2 - Papel")
    print ("3 - Tesoura")
    jogadaPlayer = int(input("Digite sua jogada: ")) - 1

def verificaVitoria():
    global jogadaComputador
    global jogadaPlayer
    global placarPlayer
    global placarComputador

    print ()
    print ("Você jogou: ",jogadas[jogadaPlayer])
    print ("O computador jogou: ",jogadas[jogadaComputador])
    print ()

#   Player joga pedra;
    if jogadaPlayer == 0:
        if jogadaComputador == 0:
            print ("Empate.")
        elif jogadaComputador == 1:
            print ("Computador venceu!")
            placarComputador += 1
        else:
            print ("Jogador venceu!")
            placarPlayer += 1

#   Player joga Papel;
    elif jogadaPlayer == 1:
        if jogadaComputador == 0:
            print ("Jogador venceu!")
            placarPlayer += 1
        elif jogadaComputador == 1:
            print ("Empate.")
        else:
            print ("Computador venceu!")
            placarComputador += 1

##  Player joga tesoura
    elif jogadaPlayer == 2:
        if jogadaComputador == 0:
            print ("Computador venceu!")
            placarComputador += 1
        elif jogadaComputador == 1:
            print ("Jogador venceu!")
            placarPlayer += 1
        else:
            print ("Empate.")

game()
verificaVitoria()
