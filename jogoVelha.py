from random import randint
import random

#random.seed(1)

def cria_jogo():
    for i in range(3):
        matriz.append([])
        for j in range(3):
            matriz[i].append("-")

def mostra_jogo():
    for i in range(len(matriz)):
        print(matriz[i])

def joga_humano():
    while True:
        linha = int(input("Digite uma linha para jogar: "))
        coluna = int(input("Digite uma coluna para jogar: "))
        if linha > 2 or linha < 0 or coluna > 2 or coluna < 0:
            print("Favor digitar entre 0 e 2.")
            continue
        elif matriz[linha][coluna] != "-":
            print("Espaço ocupado, escolha outra posição.")
            continue
        else:
            matriz[linha][coluna] = "X"
            break

def joga_computador():
    while True:
        linha = randint(0, 2)
        coluna = randint(0, 2)
        if matriz[linha][coluna] != "-":
            continue
        else:
            matriz[linha][coluna] = "O"
            break

def isJogo_acaba():
    #linha
    for i in range(len(matriz)):
        if matriz[i][0] == matriz[i][1] and matriz[i][0] == matriz[i][2] and matriz[i][0] == "X":
            return True
        elif matriz[i][0] == matriz[i][1] and matriz[i][0] == matriz[i][2] and matriz[i][0] == "O":
            return False
    #coluna
    for i in range(len(matriz)):
        if matriz[0][i] == matriz[1][i] and matriz[0][i] == matriz[2][i] and matriz[0][i] == "X":
            return True
        elif matriz[0][i] == matriz[1][i] and matriz[0][i] == matriz[2][i] and matriz[0][i] == "O":
            return False
    #diagonal 1
    if matriz[0][0] == matriz[1][1] and matriz[0][0] == matriz[2][2] and matriz[0][0] == "X":
        return True
    elif matriz[0][0] == matriz[1][1] and matriz[0][0] == matriz[2][2] and matriz[0][0] == "O":
        return False
    #diagonal 2
    if matriz[2][0] == matriz[1][1] and matriz[2][0] == matriz[0][2] and matriz[2][0] == "X":
        return True
    elif matriz[2][0] == matriz[1][1] and matriz[2][0] == matriz[0][2] and matriz[2][0] == "O":
        return False

def isJogo_empate():
    if "-" not in matriz[0] and "-" not in matriz[1] and "-" not in matriz[2]:
        return True
    else:
        return False
            
matriz = []

cria_jogo()
mostra_jogo()

while True:
    joga_humano()
    mostra_jogo()
    if isJogo_acaba() == True:
        print("Humano ganhou!")
        break
    elif isJogo_acaba() == False:
        print("Computador ganhou!")
        break
    elif isJogo_empate() == True:
        print("Empate!")
        break
    joga_computador()
    mostra_jogo()
    if isJogo_acaba() == True:
        print("Humano ganhou!")
        break
    elif isJogo_acaba() == False:
        print("Computador ganhou!")
        break
    elif isJogo_empate() == True:
        print("Empate!")
        break