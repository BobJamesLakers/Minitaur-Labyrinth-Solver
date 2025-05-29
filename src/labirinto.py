import heapq

labirinto = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1],
    [1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1],
    [1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1],
    [1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1],
    [1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1],
    [1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
    [1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1],
    [1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1],
    [1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

linhas = len(labirinto)
colunas = len(labirinto[0])

def vizinhos(pos):
    i,j = pos
    direcoes = [(-1,0), (1,0), (0,-1), (0,1)]
    for di,dj, in direcoes:
        ni, nj = i +di, j + dj
        if 0 <= ni < linhas and 0 <= nj < colunas and labirinto[ni][nj] == 0:
            yield (ni,nj)

def resolver_labirinto(inicio_idx, fim_idx):
    inicio = (inicio_idx // colunas, inicio_idx % colunas)
    fim = (fim_idx // colunas, fim_idx % colunas)

    fila = [(0, inicio)]
    dist = {inicio: 0}
    anterior = {inicio: None}

    while fila:
        custo, atual = heapq.heappop(fila)
        if atual == fim:
            break
        for viz in vizinhos(atual):
            novo_custo = dist[atual] + 1
            if viz not in dist or novo_custo < dist[viz]:
                dist[viz] = novo_custo
                anterior[viz] = atual
                heapq.heappush(fila, (novo_custo, viz))

#reconstruir o caminho
    caminho = []
    atual = fim
    while atual:
        i, j = atual
        caminho.append(i * colunas + j)
        atual = anterior.get(atual)
    caminho.reverse()

    return caminho if caminho and caminho[0] == inicio_idx else []