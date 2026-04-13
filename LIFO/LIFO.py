from livros import Livro, Autor
class LIFO:
    def __init__(self):
        self.topo = None

    def add(self, livro):
        livro.prox = self.topo
        self.topo = livro
        self.imprimir()

    def remove(self):
        if self.topo is not None:
            self.topo = self.topo.prox
        self.imprimir()

    def busca(self, nome):
        contador = 0
        aux = self.topo
    
        while aux:
            if aux.autor.nome == nome:
                contador += 1
            aux = aux.prox

        return contador

    def imprimir(self):
        print("----------------------")
        if self.topo is None:
            print("Nada para imprimir")
        else:
            print("\nPilha livros - LIFO")
            aux = self.topo
            while aux:
                print(f"""
Título: {aux.titulo}
Quantidade de páginas: {aux.paginas}
Autor: {aux.autor.nome}
Nascido da data de {aux.autor.nascimento}
""")
                aux = aux.prox
        print("----------------------")

