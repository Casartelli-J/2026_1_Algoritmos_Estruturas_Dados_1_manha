from No import No

class Lista:
    
    def __init__(self):
        self.inicio = None

    def imprimir(self):
        print("----------------")
        print("Lista encadeada por ordem crescente")
        if self.inicio is None:
            print("Lista vazia")
        else:
            aux = self.inicio
            while aux:
                print( aux.dado )
                aux = aux.prox
c kwjdfbnaui fbeaswhvb\sjhvbsvsa
    def add(self, valor):
        nodo = No(valor)
        #Inicio vazio? adiciona o nodo aqui em cima
        if self.inicio == None:
            self.inicio = nodo
            # até aqui n muda
        else:
            if nodo.dado < self.inicio.dado:
                nodo.prox = self.inicio
                self.inicio = nodo
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux:
                    if nodo.dado < aux.dado:
                        nodo.prox = aux
                        ant.prox = nodo
                        break
                    else:
                        ant = aux
                        aux = aux.prox
                if aux == None:
                    ant.prox = nodo
        self.imprimir()