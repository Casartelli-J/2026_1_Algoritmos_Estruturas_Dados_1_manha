class carro:
    
    def __init__(self, modelo = None, placa = None, ano = 2026):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.prox = None

        

    def __str__(self):
        return f"""
Modelo: {self.modelo}
Placa: {self.placa}
Ano: {self.ano}
"""
    
c = carro("Doblo", "HDK4391", 2006)
print( c )