class Apartamento:
    def __init__(self, id, numero, torre):
        self.id = id
        self.numero = numero
        self.torre = torre
        self.vaga = None  # começa sem vaga
        self.proximo = None  # lista encadeada

    def cadastrar(self):
        print(f"Apartamento {self.numero} cadastrado!")

    def imprimir(self):
        vaga_info = self.vaga if self.vaga is not None else "Sem vaga"
        print(f"ID: {self.id}, Número: {self.numero}, Vaga: {vaga_info}")