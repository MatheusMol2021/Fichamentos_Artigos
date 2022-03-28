from collections import deque
from math import inf, sqrt
import random
import operator
import time

from viewer import MazeViewer

def gera_labirinto(n_linhas, n_colunas, inicio, goal):
    # cria labirinto vazio
    labirinto = [[0] * n_colunas for _ in range(n_linhas)]

    # adiciona celulas ocupadas em locais aleatorios de
    # forma que 25% do labirinto esteja ocupado
    numero_de_obstaculos = int(0.25 * n_linhas * n_colunas)
    for _ in range(numero_de_obstaculos):
        linha = random.randint(0, n_linhas-1)
        coluna = random.randint(0, n_colunas-1)
        labirinto[linha][coluna] = 1

    # remove eventuais obstaculos adicionados na posicao
    # inicial e no goal
    labirinto[inicio.y][inicio.x] = 0
    labirinto[goal.y][goal.x] = 0

    return labirinto


class Celula:
    def __init__(self, y, x, anterior):
        self.y = y
        self.x = x
        self.anterior = anterior


def distancia(celula_1, celula_2):
    dx = celula_1.x - celula_2.x
    dy = celula_1.y - celula_2.y
    return sqrt(dx ** 2 + dy ** 2)

def distancia_A(celula_1, celula_2, custo_A):
    dx = celula_1.x - celula_2.x
    dy = celula_1.y - celula_2.y
    return (sqrt(dx ** 2 + dy ** 2) + custo_A)


def esta_contido(lista, celula):
    for elemento in lista:
        if (elemento.y == celula.y) and (elemento.x == celula.x):
            return True
    return False


def custo_caminho(caminho):
    if len(caminho) == 0:
        return inf

    custo_total = 0
    for i in range(1, len(caminho)):
        custo_total += distancia(caminho[i].anterior, caminho[i])

    return custo_total


def obtem_caminho(goal):
    caminho = []

    celula_atual = goal
    while celula_atual is not None:
        caminho.append(celula_atual)
        celula_atual = celula_atual.anterior

    # o caminho foi gerado do final para o
    # comeco, entao precisamos inverter.
    caminho.reverse()

    return caminho


def celulas_vizinhas_livres(celula_atual, labirinto):
    # generate neighbors of the current state
    vizinhos = [
        Celula(y=celula_atual.y-1, x=celula_atual.x-1, anterior=celula_atual),
        Celula(y=celula_atual.y+0, x=celula_atual.x-1, anterior=celula_atual),
        Celula(y=celula_atual.y+1, x=celula_atual.x-1, anterior=celula_atual),
        Celula(y=celula_atual.y-1, x=celula_atual.x+0, anterior=celula_atual),
        Celula(y=celula_atual.y+1, x=celula_atual.x+0, anterior=celula_atual),
        Celula(y=celula_atual.y+1, x=celula_atual.x+1, anterior=celula_atual),
        Celula(y=celula_atual.y+0, x=celula_atual.x+1, anterior=celula_atual),
        Celula(y=celula_atual.y-1, x=celula_atual.x+1, anterior=celula_atual),
    ]

    # seleciona as celulas livres
    vizinhos_livres = []
   

  #  matheus = {}
    for v in vizinhos:
                
        # verifica se a celula esta dentro dos limites do labirinto
        if (v.y < 0) or (v.x < 0) or (v.y >= len(labirinto)) or (v.x >= len(labirinto[0])):
            continue
        # verifica se a celula esta livre de obstaculos.
        if labirinto[v.y][v.x] == 0:
            vizinhos_livres.append(v)
           # matheus[(celula_atual,celula_atual)] = distancia(None,celula_atual)
           # print(matheus.values())
    return vizinhos_livres

iniciotime = time.time()

def breadth_first_search(labirinto, inicio, goal, viewer):
    # nos gerados e que podem ser expandidos (vermelhos) 
    fronteira = deque()  
    #fronteira = set()
    # nos ja expandidos (amarelos)
    expandidos = set()

    # adiciona o no inicial na fronteira
    fronteira.append(inicio)

    # variavel para armazenar o goal quando ele for encontrado.
    goal_encontrado = None

    custos = {}     # matheus e chico_menor_custo = {}
    custos1 = []

    

        
    # Repete enquanto nos nao encontramos o goal e ainda
    # existem para serem expandidos na fronteira. Se
    # acabarem os nos da fronteira antes do goal ser encontrado,
    # entao ele nao eh alcancavel.
    while (len(fronteira) > 0) and (goal_encontrado is None):

        # seleciona o no mais antigo para ser expandido
        no_atual = fronteira.popleft()
       # no_atual = custos1.pop()
       # no_atual = (min_key[1])       
        

        # busca os vizinhos do no
        vizinhos = celulas_vizinhas_livres(no_atual, labirinto)
       # vizinhos = celulas_vizinhas_livres(min_key[1], labirinto)

        # para cada vizinho verifica se eh o goal e adiciona na
        # fronteira se ainda nao foi expandido e nao esta na fronteira
 

        for v in vizinhos:
            if v.y == goal.y and v.x == goal.x:
                goal_encontrado = v
                # encerra o loop interno
                break
            else:
                if (not esta_contido(expandidos, v)) and (not esta_contido(fronteira, v)):
                    
                    custos[(inicio,v)] = distancia(inicio,v) # matheus _calcula o custo
                 #   del custos[min_key] #apaga uma chave do dicionario
                    min_key = min(custos, key = custos.get)
                    max_key = max(custos, key = custos.get)
                            
                    caminho1 = obtem_caminho(v)
                    cost1 = custo_caminho(caminho1)
                    print(cost1)


                   # fronteira.append(v)
                    fronteira.append(v)                    
                    fronteira.append(min_key[1])
                    custos1.append(min_key[1])
                    custos2 = custos1.pop()
                   # del custos2
                   # fronteira.append(v)
                    
                    
                  #  custos1.append(custos.copy)
                   # print(custos.keys())
                  #  print(f'a chave {custos.keys()} tem o valor de {custos.values()}')
                   # print(f'o valor é {(custos.values())}')
                   # print(custos.values()) #Valor do custo
                  ##  print('valor v')
                  ##  print(v)
                  ##  print()

                  #  print(inicio)
                 #   for m, n in custos.items():
                  #    print('for')
                  #    print (f'{m} = {n}')
                     # print()
                     # print()
                      
                  #  print(custos.items())
                  #  print()
                   # print(fronteira)
                  #  print()
                  #  print(no_atual)
                   # print('min')                    
                 ##   print(min_key[1], min_key)                    
                ##    print()
                 ##   print()
                    print('-' * 100)
                    print(custos2)
                    print('-' * 100)
                    print(custos)

                    #del custos[min_key[0], min_key[1]]              
                         
                 

                  #  print(custos.keys)

       # expandidos.add(no_atual)
       # fronteira.add(max_key[1])
        expandidos.add(max_key[1])
        
       # del custos[min_key[0],min_key[1]]
       # no_atual = custos1.popleft()
   
        

        viewer.update(generated=fronteira,
                      expanded=expandidos)

    caminho = obtem_caminho(goal_encontrado)
    cost = custo_caminho(caminho)
    

    return caminho, cost

fimtime = time.time()


def main():
    SEED = 24  # coloque None no lugar do 42 para deixar aleatorio
    N_LINHAS = 12
    N_COLUNAS = 16
    INICIO = Celula(y=0, x=0, anterior=None)
    GOAL = Celula(y=N_LINHAS-1, x=N_COLUNAS-1, anterior=None)

    random.seed(SEED)

    """
    O labirinto sera representado por uma matriz (lista de listas)
    em que uma posicao tem 0 se ela eh livre e 1 se ela esta ocupada.
    """
    labirinto = gera_labirinto(N_LINHAS, N_COLUNAS, INICIO, GOAL)

    viewer = MazeViewer(labirinto, INICIO, GOAL,
                        step_time_miliseconds=1, zoom=20)

    caminho, custo_total = breadth_first_search(
        labirinto, INICIO, GOAL, viewer)

    if len(caminho) == 0:
        print("Goal is unreachable for this maze.")

    print(
        f"Custo total do caminho: {custo_total}."
        f" Numero de passos: {len(caminho)-1}."
    )

    viewer.update(path=caminho)
    viewer.pause()

    print("OK!")
    print(fimtime)


if __name__ == "__main__":
    main()
