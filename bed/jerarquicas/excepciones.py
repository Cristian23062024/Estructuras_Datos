# Validar Duplicados
class DuplicateKeyError(Exception):
    def __init__(self, nueva_clave):
        super().__init__(f'La clave [{nueva_clave}] se encuentra duplicada.')

# Validar Homogeneidad
class HomogeneityError(Exception):
    def __init__(self, nueva_clave):
        super().__init__(f'La clave [{nueva_clave}] no es del mismo tipo del arbol.')
