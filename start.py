import random as rd

jogadasLista = ["Pedra", "Papel", "Tesoura"]
jogadaComputador = rd.randint(0,2)
jogadaPlayer = 0
placarPlayer = 0
placarComputador = 0

print("########################################################")

def jogadas():
    print()
    print ("1 - Pedra")
    print ("2 - Papel")
    print ("3 - Tesoura")
    print()



def jogarNovamente():
    def novamente():
        print()
        print("1 - Jogar Novamente")
        print("2 - Sair")
    novamente()
    replay = input("Deseja jogar novamente? ")
    if replay.isnumeric():
        replay = int(replay)
        if replay < 1 or replay > 2:
            jogarNovamente()
        else:
            game()
    else:
        novamente()
        replay = input("Digite apenas números: ")
        jogarNovamente()

def placar():
    print()
    print("---------------------------------------------")
    print("--                                         --")
    print("--          Seu placar: ", placarPlayer, "                --")
    print("--       Placar do computador: ", placarComputador, "         --")
    print("--                                         --")
    print("---------------------------------------------")
    print()
    jogarNovamente()

def game():
    global jogadaPlayer
    jogadas()
    jogadaPlayer = input("Digite sua jogada: ")
    verificaJogada()

def verificaJogada():
    global jogadaPlayer
    if jogadaPlayer.isnumeric():
        jogadaPlayer = int(jogadaPlayer) - 1
        if jogadaPlayer < 0 or jogadaPlayer > 2:
            jogadas()
            jogadaPlayer = input("Digite um número de 1 a 3 para escolher sua jogada: ")
            verificaJogada()
        else:
            verificaVitoria()
    else:
        jogadas()
        jogadaPlayer = input("Digite apenas números: ")
        verificaJogada()

def verificaVitoria():
    global jogadaComputador
    global jogadaPlayer
    global placarPlayer
    global placarComputador

    print ()
    print ("Você jogou: ",jogadasLista[jogadaPlayer])
    print ("O computador jogou: ",jogadasLista[jogadaComputador])
    print ()

#   Player joga pedra;
    if jogadaPlayer == 0:
        if jogadaComputador == 0:
            print ("Empate.")
            placar()
        elif jogadaComputador == 1:
            print ("Computador venceu!")
            placarComputador += 1
            placar()
        else:
            print ("Jogador venceu!")
            placarPlayer += 1
            placar()

#   Player joga Papel;
    elif jogadaPlayer == 1:
        if jogadaComputador == 0:
            print ("Jogador venceu!")
            placarPlayer += 1
            placar()
        elif jogadaComputador == 1:
            print ("Empate.")
            placar()
        else:
            print ("Computador venceu!")
            placarComputador += 1
            placar()

##  Player joga tesoura
    elif jogadaPlayer == 2:
        if jogadaComputador == 0:
            print ("Computador venceu!")
            placarComputador += 1
            placar()
        elif jogadaComputador == 1:
            print ("Jogador venceu!")
            placarPlayer += 1
            placar()
        else:
            print ("Empate.")
            placar()

game()
