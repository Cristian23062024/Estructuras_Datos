from bed.lineales.cp import ColaPrioridad

if __name__ == '__main__':
    cola = ColaPrioridad()
    
    print(cola.es_vacia())
    print('\n')
    print(cola.encolar(11, 5))
    print(cola.encolar(12, 3))
    print(cola.encolar(13, 1))
    print(cola.encolar(14, 6))
    print(cola.encolar(15, 1))
    print('\n')
    print(cola.es_vacia())
    print('\n')
    print(cola)
    print('\n')
    print(cola.desencolar())
    print('\n')
    print(cola.frente())
    print('\n')
    print(cola)
    print('\n')
    print(len(cola))
    