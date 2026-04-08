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


## FUAQ implementa uma pilha de livro.
# Cada livro deverá conter o título, a quantidade de página e 
# o autor, sendo que o autor deverá conter nome, 
# e ano de nascimento.
# Implemente um método para adicionar livros na pilha,
# um método para imprimir a pilha de livros,
# um método para remover um livro da pilha 
# e um método que o usuário informa o nome do autor e 
# lhe é informado quantos livros tem na pilha com este autor