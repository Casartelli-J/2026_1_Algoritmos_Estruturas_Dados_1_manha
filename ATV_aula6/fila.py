class FilaEspera:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar(self, apto):
        if self.fim is None:
            self.inicio = self.fim = apto
        else:
            self.fim.proximo = apto
            self.fim = apto
        apto.proximo = None

    def retirar(self):
        if self.inicio is None:
            return None

        apto = self.inicio
        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None

        return apto