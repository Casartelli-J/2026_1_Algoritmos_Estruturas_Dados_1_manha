from Carro import carro

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, car):
        if self.inicio is None:
            self.inicio = car
        else:
            self.fim.prox = car
        self.fim = car

    def imprimir(self):
        print("-----------------")
        if self.inicio is None:
            print("Fila de carros vazia")
        else:
            aux = self.inicio
            while aux:
                print( aux )
                aux = aux.prox

    def lavar(self):
        if self.inicio is None:
            print("Sem carro pra lavar")
        else:
            print("Carro lavado: ")
            print( self.inicio)
            aux = self.inicio #Mesma frescura de baixo
            self.inicio = self.inicio.prox
            del( aux ) #Isso aqui é pra liberar espaço alocado, em python isso ocorre naturalmente, mas em outras linguagens tem que forçar isso com sintaxe
            if self.inicio is None:
                self.fim = None