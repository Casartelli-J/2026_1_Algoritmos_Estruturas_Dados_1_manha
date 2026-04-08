from Nodo import No
class LIFO:
    def __init__(self):
        self.topo = None

    def add(self, dado):
        nodo = No(dado)
        if self.topo is not None:
            self.prox = self.topo
        self.topo = nodo
        self.imprimir()

    def remove(self):
        if self.topo is not None:
            self.topo = self.topo.prox
        self.imprimir()

    def imprimir(self):
        print("----------------------")
        if self.topo is None:
            print("Nada para imprimir")
        else:
            print("\nPilha - LIFO")
            aux = self.topo
            while aux:
                print( aux.dado)
                aux = aux.prox
        print("----------------------")

