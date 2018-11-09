from collections import defaultdict


class Grafo:
  def __init__(self):
    self.vertices = set()
    self.arestas = defaultdict(list)
    self.arestasOrdenadas = set()
    self.distancias = {}

  def addVertice(self, value):
    self.vertices.add(value)

  def addAresta(self, verticeOrigem, verticeDestino, distancia):
    self.arestas[verticeOrigem].append(verticeDestino)
    self.distancias[(verticeOrigem, verticeDestino)] = distancia
    self.arestas[verticeDestino].append(verticeOrigem)
    self.distancias[(verticeDestino, verticeOrigem)] = distancia
    self.arestasOrdenadas.add((distancia, verticeOrigem, verticeDestino))


parent = dict()
rank = dict()

def make_set(vertice):
  parent[vertice] = vertice
  rank[vertice] = 0

def find_set(vertice):
  if parent[vertice] != vertice:
    parent[vertice] = find_set(parent[vertice])
  return parent[vertice]

def union(origem, destino):
  root1 = find_set(origem)
  root2 = find_set(destino)
  if root1 != root2:
    if rank[root1] > rank[root2]:
      parent[root2] = root1
    else:
      parent[root1] = root2
    if rank[root1] == rank[root2]: rank[root2] += 1


def kruskal(grafo):
  A = set()

  for v in grafo.vertices:
    make_set(v)

  arestas = list(grafo.arestasOrdenadas)
  arestas.sort()

  for aresta in arestas:
    w, u, v = aresta
    if find_set(u) != find_set(v):
      union(u, v)
      A.add(aresta)

  print(' W, U, V')
  for aresta in A:
    print(aresta)

# grafo = {
#   'vertices': [0, 1, 2, 3, 4, 5, 6, 7, 8],
#   'arestas': set([
#     (1, 7, 6),
#     (2, 8, 2),
#     (2, 6, 5),
#     (4, 0, 1),
#     (4, 2, 5),
#     (6, 8, 6),
#     (7, 2, 3),
#     (7, 7, 8),
#     (8, 0, 7),
#     (8, 1, 2),
#     (9, 3, 4),
#     (10, 5, 4),
#     (11, 1, 7),
#     (14, 3, 5),
#   ])
# }
grafo = Grafo()
grafo.addVertice(0)
grafo.addVertice(1)
grafo.addVertice(2)
grafo.addVertice(3)
grafo.addVertice(4)
grafo.addVertice(5)
grafo.addVertice(6)
grafo.addVertice(7)
grafo.addVertice(8)

grafo.addAresta(7,6,1)
grafo.addAresta(8,2,2)
grafo.addAresta(6,5,2)
grafo.addAresta(0,1,4)
grafo.addAresta(2,5,4)
grafo.addAresta(6,8,6)
grafo.addAresta(2,3,7)
grafo.addAresta(7,8,7)
grafo.addAresta(0,7,8)
grafo.addAresta(1,2,8)
grafo.addAresta(3,4,9)
grafo.addAresta(5,4,10)
grafo.addAresta(1,7,11)
grafo.addAresta(3,5,14)

kruskal(grafo)
