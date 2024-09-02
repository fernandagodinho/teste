class Carro:
    def __init__(self, modelo, marca, ano, cor):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor

    def __str__(self):
        return f"Modelo: {self.modelo}, Marca: {self.marca}, Ano: {self.ano}, Cor: {self.cor}"

    def __repr__(self):
        return f"Modelo: {self.modelo}, Marca: {self.marca}, Ano: {self.ano}, Cor: {self.cor}"
    
    