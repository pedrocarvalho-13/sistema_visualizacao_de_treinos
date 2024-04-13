from .listaTreino import *
from time import sleep

visualizacao = 0

def verDetalhes(visualizacao):
    while True:
        detalhe = input("Gostaria de ver mais detalhes? (S/N)\n").upper()
        if detalhe == "S" and visualizacao == "A":
            print(detalhes["TREINO A"])
            break
        elif detalhe == "S" and visualizacao == "B":
            print(detalhes["TREINO B"])
            break
        elif detalhe == "S" and visualizacao == "C":
            print(detalhes["TREINO C"])
            break
        elif detalhe == "S" and visualizacao == "D":
            print(detalhes["TREINO D"])
            break
        elif detalhe == "S" and visualizacao == "E":
            print(detalhes["TREINO E"])
            break
        elif detalhe == "N":
            print("Você será direcionado para o menu inicial.\nAguarde um momento até que o nosso servidor te leve até lá.")
            sleep(3)
            break
        else:
            print ("Resposta invalida")


def visualizar():
    while True:
        visualizacao = str(input(f"Qual treino você gostaria de visualizar?\n{grade}\nSua Resposta: ")).upper()
        if visualizacao == "A":
            print(treino[0])
            verDetalhes(visualizacao)
            break
        elif visualizacao == "B":
            print(treino[1])
            verDetalhes(visualizacao)
            break
        elif visualizacao == "C":
            print(treino[2])
            verDetalhes(visualizacao)
            break
        elif visualizacao == "D":
            print(treino[3])
            verDetalhes(visualizacao)
            break
        elif visualizacao == "E":
            print(treino[4])
            verDetalhes()
            break
        else:
            print (f"Resposta invalida")

def sair():
    while True:
        encerrar = str(input("Deseja encerrar o programa? (S/N)")).upper()

        if encerrar == "S" or encerrar == "SIM" or encerrar == "SAIR" or encerrar == "ENCERRAR":
            break
        elif encerrar == "N" or encerrar == "NÃO" or encerrar == "NAO" or encerrar == "CONTINUAR":
            visualizar()
            continue
        else:
            print ("Resposta invalida")
            continue

print ('Bem vindo ao seu portal de treino"')