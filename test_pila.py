from bed.lineales.pila import Pila

if __name__ == '__main__':
    pila = Pila()
    pila.apilar(5)
    pila.apilar(10)
    pila.apilar(15)
    pila.apilar(10)
    pila.apilar(12)
    pila.apilar(9)
    pila.apilar(8)
    pila.apilar(10)
    pila.apilar(13)
    print('Desapilando...')
    print(pila.desapilar())
    print('\n')
    print(pila.cima())
    print(pila)
    print(pila.es_vacia())