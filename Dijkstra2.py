from collections import defaultdict
from math import inf


class Grafo:
  def __init__(self):
    self.vertices = set()
    self.arestas = defaultdict(list)
    self.distancias = {}

  def addVertice(self, value):
    self.vertices.add(value)

  def addAresta(self, verticeOrigem, verticeDestino, distancia):
    self.arestas[verticeOrigem].append(verticeDestino)
    self.distancias[(verticeOrigem, verticeDestino)] = distancia


distancia = {}
caminho = {}


def Dijkstra(grafo, verticeOrigem):
  for vertice in grafo.vertices:
    distancia[vertice] = inf
    caminho[vertice] = None
  distancia[verticeOrigem] = 0;

  vertices = set(grafo.vertices)
  while len(vertices) > 0:
    verticeMenorDistancia = menorDistancia(vertices)
    vertices.remove(verticeMenorDistancia)
    for vizinho in grafo.arestas[verticeMenorDistancia]:
      alt = distancia[verticeMenorDistancia] + grafo.distancias[(verticeMenorDistancia, vizinho)]
      if alt < distancia[vizinho]:
        distancia[vizinho] = alt
        caminho[vizinho] = verticeMenorDistancia

  print(caminho)
  menorCaminho = list()
  verticeAnterior = None
  for vertice in caminho:
    # print(vertice)
    # print(caminho[vertice])
    # print(distancia[vertice])
    if caminho[vertice] == verticeAnterior:
      menorCaminho.append(vertice)


  print(menorCaminho)


def menorDistancia(vertices):
  menorDistancia = inf
  verticeMenorDistancia = None
  for vertice in vertices:
    if distancia[vertice] < menorDistancia:
      menorDistancia = distancia[vertice]
      verticeMenorDistancia = vertice

  return verticeMenorDistancia


grafo = Grafo()

grafo.addVertice(1)
grafo.addVertice(2)
grafo.addVertice(3)
grafo.addVertice(4)
grafo.addVertice(5)
grafo.addVertice(6)

grafo.addAresta(1, 2, 7)
grafo.addAresta(1, 3, 3)
grafo.addAresta(2, 3, 1)
grafo.addAresta(2, 4, 6)
grafo.addAresta(4, 4, 4)
grafo.addAresta(3, 5, 8)
grafo.addAresta(5, 4, 2)
grafo.addAresta(5, 6, 8)
grafo.addAresta(4, 6, 2)

Dijkstra(grafo, 1)
