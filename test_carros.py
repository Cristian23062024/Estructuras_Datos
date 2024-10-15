from bed.lineales.lse import Lista_SE

class Moto:
    def __init__(self, placa, marca, modelo):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo

class Carro:
    """Clase que implementa el funcionamiento de un carro que tiene placa,
    marca, modelo. Teniendo en cuenta lo siguiente:
    - La placa debera tener un formato: 'LLL NNN' donde L es letra y N es
    numero
    - El modelo minimo valido sera 2000. Tambien el año 200 es el valor por
    defecto cuando no se pase el modelo
    """
    def __init__(self, placa, marca, modelo = 2000):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, año_modelo):
        if año_modelo < 2000:
            raise ValueError('Modelo no existe por muy antiguo!')
        else:
            self.modelo = año_modelo
            
    @property
    def placa(self):
        return self.__placa
    
    @placa.setter
    def placa(self, numero_placa):
        if numero_placa[3:5].strip() in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            raise ValueError('Numero de placa invalido')
        else:
            self.placa = numero_placa
    
    def __str__(self) -> str:
        return f'{self.placa}/{self.marca}/{self.modelo}'
    
    def __eq__(self, otro_carro):
        # if self.placa == otro_carro.placa:
        #     if self.marca == otro_carro.marca:
        #         return True
        # return False
        
        if type(self) == type(otro_carro):
            return(self.placa == otro_carro.placa and 
                   self.marca == otro_carro.marca)
        return False
        

if __name__ == "__main__":
    # lst_cars = Lista_SE()
    # car1 = Carro("ABC 123", "Renault", 1000)
    # lst_cars.adicionar(car1)
    # lst_cars.adicionar(Carro("RTY 789", "Mazda", 2010))
    # lst_cars.adicionar(Carro("QWE", "Toyota", 2002))
    # lst_cars.adicionar(Carro("PQE 852", "NIISAN", 1999))
    # lst_cars.recorrer()
    # print('')
    # print(lst_cars.encontrar(car1))
    # print(lst_cars.encontrar(Carro("PQE 852", "NIISAN", 2000)))
    # car2 = Carro("RTY 789", "Ferrari", 2001)
    # car3 = Moto("RTY 789", "Ferrari", 2012)
    # print('')
    # print(car1 == car2)
    # print(car2 == car3)
    car_1 = Carro('AAA 111', 'Mazda', 1999)
    print(car_1)
    