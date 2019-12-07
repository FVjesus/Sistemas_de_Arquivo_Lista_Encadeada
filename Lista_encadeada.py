import math
import random


def positions(blocos, tam_bloco_arq):
    posicoes = []
    n = len(blocos)

    while True:
        pos = random.randint(0, n-1)
        if(blocos[pos] == -1 and pos not in posicoes):
            posicoes.append(pos)
        if(len(posicoes) == tam_bloco_arq):
            break
    return posicoes


def verificar(tam_bloco_arq, blocos):
    cont = 0
    for i in range(len(blocos)):
        if(blocos[i] == -1):
            cont = cont + 1

    if(cont >= tam_bloco_arq):
        return True
    else:
        return False


def allocation(blocos, bitmpa, tam_arq, tam_bloco):
    for i in range(len(tam_arq)):
        tam_bloco_arq = math.ceil(tam_arq[i]/tam_bloco)
        if(verificar(tam_bloco_arq, blocos)):
            posicoes = positions(blocos, tam_bloco_arq)
            name = 'arquivo '+str(i+1)
            for j in range(len(posicoes)):
                bitmpa[posicoes[j]] = 1
                if((j + 1) < len(posicoes)):
                    blocos[posicoes[j]] = (name,posicoes[j+1]+1)
                else:
                    blocos[posicoes[j]] = (name, None)
        else:
            print("\nEspaço insuficiente para o arquivo "  + str(i + 1))
    return


def main():
    print("Defina a quantidade de blocos")
    qntd_blocos = int(input())
    print("Defina o tamanho de cada bloco")
    tam_bloco = float(input())
    print("Defina a quantidade de arquivos")
    arq_qntd = int(input())
    print("Defina o tamanho de cada arquivo")

    blocos = [-1]*qntd_blocos
    bitmap = [0]*qntd_blocos
    tam_arq = []
    for i in range(arq_qntd):
        print("arquivo", i+1, "tamanho")
        tam_arq.append(float(input()))

    allocation(blocos, bitmap, tam_arq, tam_bloco)

    print('\n',blocos)
    print('\n',bitmap)

main()