class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __gt__(self, otra_persona):
        return self.nombre > otra_persona.nombre
    
    def __lt__(self, otra_persona):
        return self.nombre < otra_persona.nombre
        
    def __str__(self):
        return f'Nombre: {self.nombre}; Edad: {self.edad} años'
    
# if __name__ == '__main__':
#     p1 = Persona('Juan', 10)
#     p2 = Persona('Carolina', 20)
    
#     print(p1 > p2) #p1.__gt__(p2)
#     print(p1 < p2) # p2.__gt__(p1) p1.__lt__(p2)