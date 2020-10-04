from random import randint
import random

#random.seed(1)

tabuleiro = {"A1": "-", "A2": "-", "A3": "-",
             "B1": "-", "B2": "-", "B3": "-",
             "C1": "-", "C2": "-", "C3": "-"}

posicoes = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

def mostra_tabuleiro_inicio():
    print("A1" + "|" + "A2" + "|" + "A3")
    print("--+--+--")
    print("B1" + "|" + "B2" + "|" + "B3")
    print("--+--+--")
    print("C1" + "|" + "C2" + "|" + "C3")

def mostra_tabuleiro():
    print(tabuleiro["A1"] + "|" + tabuleiro["A2"] + "|" + tabuleiro["A3"])
    print("-+-+-")
    print(tabuleiro["B1"] + "|" + tabuleiro["B2"] + "|" + tabuleiro["B3"])
    print("-+-+-")
    print(tabuleiro["C1"] + "|" + tabuleiro["C2"] + "|" + tabuleiro["C3"])

def joga_humano():
    while True:
        posicao = input("Em qual posição gostaria de jogar? ").title()
        if posicao in posicoes:
            if "-" in tabuleiro[posicao]:
                tabuleiro[posicao] = "X"
                break
            else:
                print("Posição já ocupada, informe outra posição!")
                continue
        else:
            print("Essa posição não existe, informe outra posição!")
            continue

def joga_computador():
    while True:
        valor = randint(0, 8)
        posicao = posicoes[valor]
        if "-" in tabuleiro[posicao]:
            tabuleiro[posicao] = "O"
            break
        else:
            continue

def isJogo_acaba():
    #Linhas
    if tabuleiro["A1"] == tabuleiro["A2"] and tabuleiro["A1"] == tabuleiro["A3"] and tabuleiro["A1"] == "X":
        return True
    elif tabuleiro["A1"] == tabuleiro["A2"] and tabuleiro["A1"] == tabuleiro["A3"] and tabuleiro["A1"] == "O":
        return False
    elif tabuleiro["B1"] == tabuleiro["B2"] and tabuleiro["B1"] == tabuleiro["B3"] and tabuleiro["B1"] == "X":
        return True
    elif tabuleiro["B1"] == tabuleiro["B2"] and tabuleiro["B1"] == tabuleiro["B3"] and tabuleiro["B1"] == "O":
        return False
    elif tabuleiro["C1"] == tabuleiro["C2"] and tabuleiro["C1"] == tabuleiro["C3"] and tabuleiro["C1"] == "X":
        return True
    elif tabuleiro["C1"] == tabuleiro["C2"] and tabuleiro["C1"] == tabuleiro["C3"] and tabuleiro["C1"] == "O":
        return False
    #Colunas
    if tabuleiro["A1"] == tabuleiro["B1"] and tabuleiro["A1"] == tabuleiro["C1"] and tabuleiro["A1"] == "X":
        return True
    elif tabuleiro["A1"] == tabuleiro["B1"] and tabuleiro["A1"] == tabuleiro["C1"] and tabuleiro["A1"] == "O":
        return False
    elif tabuleiro["A2"] == tabuleiro["B2"] and tabuleiro["A2"] == tabuleiro["C2"] and tabuleiro["A2"] == "X":
        return True
    elif tabuleiro["A2"] == tabuleiro["B2"] and tabuleiro["A2"] == tabuleiro["C2"] and tabuleiro["A2"] == "O":
        return False
    elif tabuleiro["A3"] == tabuleiro["B3"] and tabuleiro["A3"] == tabuleiro["C3"] and tabuleiro["A3"] == "X":
        return True
    elif tabuleiro["A3"] == tabuleiro["B3"] and tabuleiro["A3"] == tabuleiro["C3"] and tabuleiro["A3"] == "O":
        return False
    #Diagonais
    if tabuleiro["A1"] == tabuleiro["B2"] and tabuleiro["A1"] == tabuleiro["C3"] and tabuleiro["A1"] == "X":
        return True
    elif tabuleiro["A1"] == tabuleiro["B2"] and tabuleiro["A1"] == tabuleiro["C3"] and tabuleiro["A1"] == "O":
        return False
    elif tabuleiro["A3"] == tabuleiro["B2"] and tabuleiro["A3"] == tabuleiro["C1"] and tabuleiro["A3"] == "X":
        return True
    elif tabuleiro["A3"] == tabuleiro["B2"] and tabuleiro["A3"] == tabuleiro["C1"] and tabuleiro["A3"] == "O":
        return False

def isJogo_empate():
    qtd = 0
    for values in tabuleiro.values():
        if values != "-":
            qtd += 1
    if qtd == 9:
        return True
    else:
        return False

while True:
    print("Posições do jogo:")
    mostra_tabuleiro_inicio()
    print()
    mostra_tabuleiro()
    joga_humano()
    print()
    mostra_tabuleiro()
    if isJogo_acaba() == True:
        print("Humano ganhou!")
        break
    elif isJogo_empate() == True:
        print("Empate...")
        break
    joga_computador()
    print()
    if isJogo_acaba() == False:
        mostra_tabuleiro()
        print("Computador ganhou!")
        break
    elif isJogo_empate() == True:
        mostra_tabuleiro()
        print("Empate...")
        break