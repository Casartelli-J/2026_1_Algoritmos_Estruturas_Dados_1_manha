from apt import Apartamento
from torre import Torre 
from lista import ListaApartamentos, liberar_vaga
from fila import FilaEspera 

torre1 = Torre(1, "Torre A", "Rua X")

ap1 = Apartamento(1, "101", torre1)
ap2 = Apartamento(2, "102", torre1)
ap3 = Apartamento(3, "103", torre1)

fila = FilaEspera()
lista = ListaApartamentos()

ap1.vaga = 1
ap2.vaga = 2

lista.inserir_ordenado(ap1)
lista.inserir_ordenado(ap2)

fila.adicionar(ap3)

liberar_vaga(ap1, fila, lista)

print("\nLista de apartamentos com vaga:")
lista.imprimir()