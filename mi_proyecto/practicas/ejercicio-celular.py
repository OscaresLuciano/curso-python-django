class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.bateria = 100

    def usar(self):
        self.bateria -= 10
        print(f"Queda %{self.bateria} de batería")

    def cargar(self):
        self.bateria = 100
        print(f"Batería cargada")

celular1 = Celular("Motorola", "Edge 60 pro")

celular1.usar()
celular1.usar()
celular1.cargar()