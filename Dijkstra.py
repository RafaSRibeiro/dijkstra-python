from collections import defaultdict

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


def dijsktra(grafo, inicio):
  visitado = {inicio: 0}
  caminho = {}

  vertices = set(grafo.vertices)

  while vertices:
    menorAresta = None
    for vertice in vertices:
      if vertice in visitado:
        if menorAresta is None:
          menorAresta = vertice
        elif visitado[vertice] < visitado[menorAresta]:
          menorAresta = vertice

    if menorAresta is None:
      break

    vertices.remove(menorAresta)
    pesoAtual = visitado[menorAresta]

    for aresta in grafo.arestas[menorAresta]:
      peso = pesoAtual + grafo.distancias[(menorAresta, aresta)]
      if aresta not in visitado or peso < visitado[aresta]:
        visitado[aresta] = peso
        caminho[aresta] = menorAresta

  return visitado, caminho

valoresParaTeste = True if input("Valoes de Teste (Padrão: Não): (Sim|Não)") == 'Sim' else False

grafo = Grafo()

if valoresParaTeste:
  grafo.addVertice('A')
  grafo.addVertice('B')
  grafo.addVertice('C')
  grafo.addVertice('D')
  grafo.addVertice('E')

  grafo.addAresta('A','B',1)
  grafo.addAresta('B','C',1)
  grafo.addAresta('B','D',2)
  grafo.addAresta('D','E',1)
  grafo.addAresta('C','E',5)
  grafo.addAresta('A','E',2)

  origem = 'A'
else:
  valorado = True if input("Grafo valorado (Padrão: Não): (Sim|Não)") == 'Sim' else False
  orientado = True if input("Grafo orientado (Padrão: Não): (Sim|Não)") == 'Sim' else False

  while True:
    vertice = input("Arestas (Ex: A): ")
    if vertice == '':
      break
    grafo.addVertice(vertice)

  print(grafo.vertices, flush=True)

  while True:
    arestaOrigem = input("Origem: ")
    if arestaOrigem == '':
      break

    arestaDestino = input("Destino: ")

    if valorado:
      peso = int(input("Peso/Valor (numerico): "))
    else:
      peso = 1

    grafo.addAresta(arestaOrigem, arestaDestino, peso)
    if not orientado:
      grafo.addAresta(arestaDestino, arestaOrigem, peso)

  origem = input("Vertice de origem: ")

resultado = dijsktra(grafo, str(origem))

visitados = resultado[0]
caminho = resultado[1]

print("| Vertice | Distancia |   Path |")
for visitado in visitados:
  try:
    path = caminho[visitado]
  except KeyError:
    path = 0
  print('|', visitado.rjust(6),' |', str(visitados[visitado]).rjust(8),' |', str(path).rjust(5), ' |')
