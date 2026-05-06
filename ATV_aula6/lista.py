class ListaApartamentos:
    def __init__(self):
        self.inicio = None

    def inserir_ordenado(self, apto):
        if self.inicio is None or apto.vaga < self.inicio.vaga:
            apto.proximo = self.inicio
            self.inicio = apto
        else:
            atual = self.inicio
            while atual.proximo and atual.proximo.vaga < apto.vaga:
                atual = atual.proximo

            apto.proximo = atual.proximo
            atual.proximo = apto

    def imprimir(self):
        atual = self.inicio
        while atual:
            atual.imprimir()
            atual = atual.proximo


def liberar_vaga(apto, fila, lista):
    print(f"\nApartamento {apto.numero} liberou vaga {apto.vaga}")

    # Coloca na fila
    fila.adicionar(apto)

    # Passa a vaga para o primeiro da fila
    proximo_apto = fila.retirar()

    if proximo_apto:
        proximo_apto.vaga = apto.vaga
        lista.inserir_ordenado(proximo_apto)
        print(f"Vaga {apto.vaga} atribuída ao apto {proximo_apto.numero}")

    apto.vaga = None