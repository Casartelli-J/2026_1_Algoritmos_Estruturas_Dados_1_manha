from LIFO import LIFO
from livros import Autor, Livro
lifo = LIFO()

autista = Autor("Dom casmurro", 1981)
livrinho = Livro("Memorias cu", 190, autista)
autist = Autor("Arnaldo duarte", 1451)
livro = Livro("Novo testamento", 865, autist)
austa = Autor("Dom cas", 1911)
lin = Livro("Memoria", 190, austa)
utista = Autor("Dom casmurro", 1981)
linho = Livro("Memorias Arnaldo", 190, utista)


lifo.add(livrinho)
lifo.add(livro)
lifo.add(linho)
lifo.add(lin)

lifo.imprimir()

lifo.busca("Dom casmurro")



