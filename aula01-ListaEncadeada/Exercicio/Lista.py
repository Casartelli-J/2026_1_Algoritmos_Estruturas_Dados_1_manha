from No import No
# Lista duplamente encadeada por ordem de chegada

class ListaDuplamente:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def imprimir(self):
        print("----------------")
        print("Lista Duplamente encadeada por ordem de chegada")
        if self.inicio is None:
            print("Lista vazia")
        else:
            aux = self.inicio
            while aux:
                print( aux.dado )
                aux = aux.proximo

    def imprimirReverso(self):
        print("----------------")
        print("Lista Duplamente encadeada por ordem de chegada Reversa")
        if self.inicio is None:
          print("Lista vazia")
        else:
            aux = self.fim
            while aux:
                print( aux.dado )
                aux = aux.anterior


    def add(self, valor):
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
        else:
            if nodo.dado < self.inicio.dado:
                nodo.proximo = self.inicio
                self.inicio = nodo
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux:
                    if nodo.dado < aux.dado:
                        nodo.proximo = aux
                        aux.anterior = nodo
                        ant.proximo = nodo
                        nodo.anterior = ant
                        break
                    else:
                        ant = aux
                        aux.anterior = ant
                        aux = aux.proximo
                        
                if aux == None:
                    ant.proximo = nodo



        self.fim = nodo    
        self.imprimir()