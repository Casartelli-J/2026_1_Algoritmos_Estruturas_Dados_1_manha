"""
Construa um software em Python que implemente uma Pilha de carros e uma Pilha de drones. Feito

As classes carro e drone herdam da classe veículo os atributos e comuns às duas classes. Feito

A classe carro é composta dos atributos marca, modelo e portas. O atributo portas é fracamente privado. Feito + / -

A classe drone é composta dos atributos marca, modelo e quantidade de hélices. O atributo quantidade de hélices é fortemente privado. Feito + / -

Todas classes devem ter um método para imprimir as informações dos seus respectivos atributos. Feito

Implemente uma tela com um menu (funcionando) que permita ao usuário:

-> Adicionar e remover carros da Pilha.

-> Adicionar e remover drones da Pilha.

-> Imprimir a Pilha de carros e a Pilha de drones.

Cole todo código desenvolvido, em sequência, separando as classes por uma linha.
"""
###########################
######    OBJETOS    ######
###########################
class veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def imprimir(self):
        pass

class drone(veiculo):
    def __init__(self, marca, modelo, qtd_helices):
        super().__init__(marca, modelo)
        self.qtd_helices = qtd_helices
        self.prox = None
    def imprimir(self):
        print("------------------------")
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nQuantidade de hélices: {self.qtd_helices}")
        print("------------------------")

class carro(veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas
        self.prox = None

    def imprimir(self):
        print("------------------------")
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nQuantidade de portas: {self.portas}")
        print("------------------------")

########################
#####   LISTAS   #######
########################
class pCarro:
    def __init__(self):
        self.topo = None

    def imprimir(self):
        if self.topo == None:
            print("Não tem nada")
        else:
            aux = self.topo
            print("------------------------")
            print("Pilha de Carros:")
            while aux:
                print(aux.modelo)
                aux = aux.prox
            print("------------------------")

    def add(self, carro):
        if self.topo == None:
            self.topo = carro
        else:
            carro.prox = self.topo
            self.topo = carro
        self.imprimir()

    def remover(self):
        if self.topo == None:
            print("Pilha vazia")
        else:
            self.topo = self.topo.prox
        self.imprimir()

class pDrone:
    def __init__(self):
        self.topo = None

    def imprimir(self):
        if self.topo == None:
            print("Não tem nada")
        else:
            aux = self.topo
            print("------------------------")
            print("Pilha de Drones:")
            while aux:
                print(aux.modelo)
                aux = aux.prox
            print("------------------------")

    def add(self, drone):
        if self.topo == None:
            self.topo = drone
        else:
            drone.prox = self.topo
            self.topo = drone
        self.imprimir()

    def remover(self):
        if self.topo == None:
            print("Pilha vazia")
        else:
            self.topo = self.topo.prox
        self.imprimir()


#########################
######   RESTO    #######
#########################
def criaCarro():
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    try:
        porta = int(input("Quantidade de portas: "))
    except:
        print("Utilize números!")
    
    car = carro(marca, modelo, porta)
    return car

def criaDrone():
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    try:
        qtd_helices = int(input("Quantidade de portas: "))
    except:
        print("Utilize números!")
    
    dron = drone(marca, modelo, qtd_helices)
    return dron


pilhaC = pCarro()
pilhaD = pDrone()
carro1 = carro("teste", "teste1", 5)
carro2 = carro("teste", "teste2", 5)
carro3 = carro("teste", "teste3", 5)
carro4 = carro("teste", "teste4", 5)
pilhaC.add(carro1)
pilhaC.add(carro2)
pilhaC.add(carro3)
pilhaC.add(carro4)
drone1 = drone("teste", "teste1", 5)
drone2 = drone("teste", "teste2", 5)
drone3 = drone("teste", "teste3", 5)
drone4 = drone("teste", "teste4", 5)
pilhaD.add(drone1)
pilhaD.add(drone2)
pilhaD.add(drone3)
pilhaD.add(drone4)
def programa():
    loop = 1
    while loop == 1:
        print("""
        ############################################
        ## Sistema de Pilha de Drone e de Carros! ##
        ############################################
        #   OPÇÕES   
        #   
        #   1.Adicionar Carro
        #   2.Adicionar Drone
        #
        #   3.Remover Carro
        #   4.Remover Drone
        #
        #   5.Imprimir a pilha de Carros
        #   6.Imprimir a pilha de Drones
        #
        #   0.Terminar programa
    """)
        try:
            escolha = int(input("Escolha: "))
        except:
            print("Utilize números.")

        if escolha == 1:
            car = criaCarro()
            pilhaC.add(car)
            input()
        elif escolha == 2:
            dron = criaDrone()
            pilhaD.add(dron)
            input()
        elif escolha == 3:
            pilhaC.remover()
            input()
        elif escolha == 4:
            pilhaD.remover()
            input()
        elif escolha == 5:
            pilhaC.imprimir()
            input()
        elif escolha == 6:
            pilhaD.imprimir()
            input()
        elif escolha == 0:
            print("Programa finalizado!")
            loop = 0
            input()
        else:
            print("Utilize números de 0 a 6 por favor.")
            input()

programa()
            


