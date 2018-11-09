from collections import defaultdict
from math import inf

class Grafo:
  def __init__(self):
    self.vertices = set()
    self.arestas = defaultdict(list)
    self.peso = {}

  def addVertice(self, value):
    self.vertices.add(value)

  def addAresta(self, verticeOrigem, verticeDestino, peso):
    self.arestas[verticeOrigem].append(verticeDestino)
    self.peso[(verticeOrigem, verticeDestino)] = peso
    self.arestas[verticeDestino].append(verticeOrigem)
    self.peso[(verticeDestino, verticeOrigem)] = peso

chave = {}
pai = {}
arvConj = list()

def extractMin(Q):
  menorVertice = None
  for vertice in Q:
    if menorVertice == None:
      menorVertice = vertice
    elif chave[vertice] < chave[menorVertice]:
      menorVertice = vertice
  Q.remove(menorVertice)
  return menorVertice

def MSTPrim(grafo, menorVertice):
  for vertice in grafo.vertices:
    chave[vertice] = inf
    pai[vertice] = None
  chave[menorVertice] = 0

  Q = list(grafo.vertices)
  while len(Q) > 0:
    u = extractMin(Q)
    print(u)
    for v in grafo.arestas[u]:
      if v in Q and grafo.peso[(u,v)] < chave[v]:
        pai[u]
        chave[v] = grafo.peso[(u,v)]
  print(chave)
  total = 0
  for v in chave:
    total += chave[v]
  print(total)

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
grafo.addAresta(7,8,8)
grafo.addAresta(0,7,8)
grafo.addAresta(1,2,9)
grafo.addAresta(3,4,9)
grafo.addAresta(5,4,10)
grafo.addAresta(1,7,11)
grafo.addAresta(3,5,14)


MSTPrim(grafo, 0)
