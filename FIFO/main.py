from Carro import carro
from FIla import Fila

fila = Fila()

op = -1
while op != 0:
    print("""
 1) Adicionar fila
 2) Imprimir Carro
 3) Lavar Carro
 0) Sair
""")
    op = int(input("Digite sua opção: "))

    if op == 1:
        Carro = carro()
        Carro.modelo = input("Modelo: ")
        Carro.placa = input("Placa: ")
        Carro.ano = int(input("Ano: "))
        fila.add(Carro)
    
    elif op == 2:
        fila.imprimir()

    elif op == 3:
        fila.lavar()

    elif op < 0 or op > 3:
        print("Selecione ")